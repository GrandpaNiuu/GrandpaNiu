# GrandpaNiu Fusion Policy

GrandpaNiu uses a single public module strategy. The public entry is `Ronghemokuai.sgmodule`; all source review, generation and reports must serve that one fusion output.

## 1. Public module rule

- Public users should be directed to one module: `Ronghemokuai.sgmodule`.
- `Release/Module.sgmodule` may remain as an alias for compatibility.
- Per-App modules under `Release/Modules/` are diagnostic and convenience slices, not separate product versions.
- Reserved channel folders may exist for build compatibility, but they are not the main user-facing strategy.

## 2. Fusion admission rule

A source may enter the fusion module only when it has a clear purpose and a traceable origin.

Before promotion into `Rewrite/Sources/Apps/`, `Rewrite/Sources/Misc/`, `Rules/` or `Scripts/`, record or confirm:

- source or upstream name
- target App or service
- expected benefit
- affected section: Rule, URL Rewrite, Header Rewrite, Body Rewrite, Map Local, Script or MITM
- risk level: `low`, `medium`, `high`, or `critical`
- rollback path

## 3. Candidate-first rule

Unproven material goes into `Rewrite/Sources/Candidates/` first. It does not enter the public module until reviewed.

Promotion path:

```text
upstream idea
    -> Rewrite/Sources/Candidates/
    -> review for duplication, risk and scope
    -> Rewrite/Sources/Apps/ or Rewrite/Sources/Misc/
    -> Builder.py
    -> Ronghemokuai.sgmodule
```

Rejected or deferred material goes into `Rewrite/Sources/Rejected/` with the reason preserved.

## 4. Protection rule

The fusion module should prefer stability over maximum blocking. Core account, wallet, playback and static asset endpoints should be protected by dedicated `Rules/protect-*.list` files and loaded early in `Rewrite/Profiles/fusion.conf`.

Current protection files:

- `Rules/protect-login.list`
- `Rules/protect-payment.list`
- `Rules/protect-video.list`
- `Rules/protect-cdn.list`

These files should stay conservative. Do not add ad, analytics or promotion domains to protection lists.

## 5. Rewrite and MITM rule

Rules are easier to roll back than deep rewrite behavior. For the fusion module:

- Domain and rule-list entries are preferred when they solve the issue.
- Script, Body Rewrite, Header Rewrite and MITM entries require a stronger reason.
- Broad matching should be avoided.
- Anything likely to affect account state, payment state, media playback or core app navigation needs manual validation before release.

## 6. Release rule

The normal build command remains:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

The expected public result remains one main module:

```text
Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
Release/Module.sgmodule
```

Do not create new public module families unless the project strategy is explicitly changed.
