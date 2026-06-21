#!/usr/bin/env bash
set -euo pipefail

lock_ref="${AUTOMATION_LOCK_REF:-refs/heads/automation-maintenance-lock}"
state_file="$(git rev-parse --git-path automation-maintenance-lock)"

if [ ! -f "$state_file" ]; then
  echo "No automation lock state found; nothing to release."
  exit 0
fi

lock_sha="$(tr -d '\r\n' < "$state_file")"
if [ -z "$lock_sha" ]; then
  echo "Automation lock state is empty; refusing an unguarded delete." >&2
  exit 1
fi

remote_sha="$(git ls-remote --heads origin "$lock_ref" | awk 'NR == 1 {print $1}')"
if [ -z "$remote_sha" ]; then
  rm -f "$state_file"
  echo "Automation lock is already absent."
  exit 0
fi

if [ "$remote_sha" != "$lock_sha" ]; then
  echo "Automation lock ownership changed; refusing to delete ${remote_sha}." >&2
  exit 1
fi

git push --quiet \
  --force-with-lease="${lock_ref}:${lock_sha}" \
  origin ":${lock_ref}"
rm -f "$state_file"
echo "Released automation lock ${lock_sha}."
