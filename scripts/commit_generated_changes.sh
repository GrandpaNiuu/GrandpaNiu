#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <commit-message> <path> [<path> ...]" >&2
  exit 2
fi

message="$1"
shift

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

git add -- "$@"
if git diff --cached --quiet; then
  echo "No generated changes to commit."
  exit 0
fi

git commit -m "$message"

for attempt in 1 2 3; do
  if git push origin HEAD:main; then
    exit 0
  fi
  echo "Push failed on attempt ${attempt}; rebasing on origin/main and retrying."
  git fetch origin main
  if ! git rebase origin/main; then
    git rebase --abort || true
    echo "Rebase conflict; refusing to overwrite generated files." >&2
    exit 1
  fi
done

echo "Push failed after 3 attempts."
exit 1
