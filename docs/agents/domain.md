# Domain Docs

This repo uses a single-context domain documentation layout.

Engineering skills that diagnose bugs, improve architecture, write tests, or prepare product work should use the files below to learn the project language and prior decisions.

## Before exploring, read these

- `CONTEXT.md` at the repo root, if it exists
- `docs/adr/`, if it exists, especially ADRs that touch the area being changed

If these files do not exist, proceed silently. Do not block work just because they are missing, and do not create them unless the current task is specifically about domain modeling or architecture decisions.

## Expected layout

```text
/
|-- CONTEXT.md
|-- docs/
|   `-- adr/
|       |-- 0001-example-decision.md
|       `-- 0002-example-follow-up.md
```

## Use the glossary's vocabulary

When output names a domain concept, such as in an issue title, refactor proposal, test name, or bug hypothesis, prefer the wording defined in `CONTEXT.md`.

If the concept is not in the glossary yet, either use the existing repository wording from nearby docs/code or note that the glossary has a gap for later domain modeling.

## Flag ADR conflicts

If a recommendation or code change contradicts an existing ADR, surface it explicitly instead of silently overriding the decision.
