# Issue tracker: GitHub

This repo tracks work in GitHub Issues. Use the `gh` CLI for issue operations when a skill needs to read, create, update, label, or close work items.

## Conventions

- Create an issue: `gh issue create --title "..." --body "..."`
- Read an issue: `gh issue view <number> --comments`
- List issues: `gh issue list --state open --json number,title,body,labels,comments`
- Comment on an issue: `gh issue comment <number> --body "..."`
- Apply or remove labels: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- Close an issue: `gh issue close <number> --comment "..."`

Run `gh` commands from inside this repository so it can infer `GrandpaNiuu/GrandpaNiu` from `git remote -v`.

## Pull requests as a triage surface

PRs as a request surface: yes.

External PRs should be triaged through the same labels and states as issues. Use the `gh pr` equivalents:

- Read a PR: `gh pr view <number> --comments`
- Inspect a PR diff: `gh pr diff <number>`
- List external PRs for triage: `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`
- Keep external request sources such as `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE`
- Do not pull collaborator in-flight PRs into the triage queue by default: skip `OWNER`, `MEMBER`, and `COLLABORATOR`
- Comment, label, or close with `gh pr comment`, `gh pr edit --add-label` / `--remove-label`, and `gh pr close`

GitHub shares one number space across issues and PRs. When a bare reference such as `#42` is ambiguous, try `gh pr view 42` first and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`, unless the ticket is clearly a PR, in which case use `gh pr view <number> --comments`.
