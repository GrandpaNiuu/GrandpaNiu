#!/usr/bin/env bash
set -euo pipefail

lock_ref="${AUTOMATION_LOCK_REF:-refs/heads/automation-maintenance-lock}"
max_attempts="${AUTOMATION_LOCK_ATTEMPTS:-240}"
sleep_seconds="${AUTOMATION_LOCK_SLEEP_SECONDS:-15}"
stale_seconds="${AUTOMATION_LOCK_STALE_SECONDS:-3600}"
state_file="$(git rev-parse --git-path automation-maintenance-lock)"
remote_lock_ref="refs/remotes/origin/automation-maintenance-lock"

require_positive_integer() {
  local name="$1"
  local value="$2"
  if ! [[ "$value" =~ ^[1-9][0-9]*$ ]]; then
    echo "${name} must be a positive integer, got: ${value}" >&2
    exit 2
  fi
}

require_positive_integer "AUTOMATION_LOCK_ATTEMPTS" "$max_attempts"
require_positive_integer "AUTOMATION_LOCK_SLEEP_SECONDS" "$sleep_seconds"
require_positive_integer "AUTOMATION_LOCK_STALE_SECONDS" "$stale_seconds"

if [ -n "$(git status --porcelain --untracked-files=normal)" ]; then
  echo "Refusing to acquire the automation lock with a dirty checkout." >&2
  exit 1
fi

git fetch --quiet origin main

for ((attempt = 1; attempt <= max_attempts; attempt++)); do
  base_sha="$(git rev-parse refs/remotes/origin/main)"
  tree_sha="$(git rev-parse "${base_sha}^{tree}")"
  lock_message="automation maintenance lock: ${GITHUB_RUN_ID:-local}-${GITHUB_RUN_ATTEMPT:-1}"
  lock_sha="$({ printf '%s\n' "$lock_message"; } | \
    GIT_AUTHOR_NAME='github-actions[bot]' \
    GIT_AUTHOR_EMAIL='github-actions[bot]@users.noreply.github.com' \
    GIT_COMMITTER_NAME='github-actions[bot]' \
    GIT_COMMITTER_EMAIL='github-actions[bot]@users.noreply.github.com' \
    git commit-tree "$tree_sha" -p "$base_sha")"

  if git push --quiet origin "${lock_sha}:${lock_ref}"; then
    printf '%s\n' "$lock_sha" > "$state_file"
    git fetch --quiet origin main
    git merge --ff-only refs/remotes/origin/main
    echo "Acquired automation lock ${lock_sha} on attempt ${attempt}."
    exit 0
  fi

  if git fetch --quiet origin "+${lock_ref}:${remote_lock_ref}" 2>/dev/null; then
    existing_sha="$(git rev-parse "$remote_lock_ref")"
    lock_epoch="$(git show -s --format=%ct "$existing_sha")"
    now_epoch="$(date +%s)"
    lock_age="$((now_epoch - lock_epoch))"
    if [ "$lock_age" -ge "$stale_seconds" ]; then
      echo "Removing stale automation lock ${existing_sha} (${lock_age}s old)."
      git push --quiet \
        --force-with-lease="${lock_ref}:${existing_sha}" \
        origin ":${lock_ref}" || true
      continue
    fi
  fi

  if [ "$attempt" -lt "$max_attempts" ]; then
    echo "Automation lock is busy; waiting ${sleep_seconds}s (${attempt}/${max_attempts})."
    sleep "$sleep_seconds"
    git fetch --quiet origin main
  fi
done

echo "Timed out waiting for ${lock_ref}." >&2
exit 1
