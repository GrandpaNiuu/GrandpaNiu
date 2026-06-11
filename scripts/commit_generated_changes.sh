#!/usr/bin/env bash
set -euo pipefail

message="${1:-Update generated fusion outputs}"

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

for attempt in 1 2 3; do
  git add -A
  if git diff --cached --quiet; then
    echo "No generated changes to commit."
    exit 0
  fi
  git commit -m "$message"
  if git push origin HEAD:main; then
    exit 0
  fi
  echo "Push failed on attempt ${attempt}; rebasing with generated output preference."
  git fetch origin main
  if git rebase -X theirs origin/main; then
    if git push origin HEAD:main; then
      exit 0
    fi
  else
    git rebase --abort || true
    git fetch origin main
    git reset --hard origin/main
  fi
done

echo "Push failed after 3 attempts."
exit 1
