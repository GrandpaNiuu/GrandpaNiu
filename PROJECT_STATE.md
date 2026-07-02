# GrandpaNiu Project State

Last updated: 2026-07-02 09:57 +08:00

## 2026-07-02 Automation Repair Snapshot

- Local branch was fast-forwarded to current `origin/main` before repair.
- The automation failure was caused by stale governance validation after active Stable / Stable Plus / Lite / Full artifacts were retired.
- `scripts/validate_governance_extensions.py` now validates the current Fusion-only policy contract.
- `docs/PROFILE_POLICY.md` now describes Fusion-only publishing and generated-output boundaries without old gate wording.
- No traffic rules, MITM scopes, App sources, Android routing policy, Windows routing policy, or public entry names were intentionally changed.
- Local validation passed:
  - `python Rewrite/Generator/Builder.py --profile fusion --release --check`
  - `python scripts/quality_gate.py`
  - `python scripts/validate_repository.py`
  - `python scripts/repository_health_check.py`
- `reports/automation_status_report.md` currently reports required scheduled workflows as `ok`; push validation should be checked after publishing this repair.

GrandpaNiu 鏄竴涓?source-first 瑙勫垯鏋勫缓浠撳簱锛岃緭鍑?iOS Fusion 妯″潡銆丄ndroid 瑙勫垯鏍煎紡銆乄indows v2rayN 璺敱銆乄eb catalog 涓庢不鐞嗘姤鍛娿€?
褰撳墠鍞竴鍏紑 iOS 璺緞鏄?Fusion锛歚Ronghemokuai.sgmodule`銆乣Release/Ronghemokuai.sgmodule` 涓?`Release/Module.sgmodule`銆?
Stable銆丼table Plus銆丩ite 鍜?Full 鐨?profile銆丷elease 鏂囦欢銆佹檵绾ц剼鏈強鏃ф祴璇曟姤鍛婂凡琚Щ闄ゃ€傚巻鍙茬姸鎬佷粎閫氳繃 Git 鎻愪氦杩芥函銆?
鏃ュ父缁存姢婧愬ご鏄?`Rules/`銆乣Scripts/`銆乣Rewrite/Sources/`銆乣Rewrite/Remotes/` 涓?`Rewrite/Profiles/fusion.conf`銆俙Release/`銆乣Web/`銆乣reports/` 涓庢牴鐩綍妯″潡鍧囦负鐢熸垚鐗┿€?
鏍囧噯缁存姢璺緞锛欶usion 鏋勫缓鍣ㄣ€佷粨搴撻獙璇併€佽川閲忛棬銆佸仴搴锋鏌ャ€備换浣曡鍒欍€佽剼鏈€丮ITM 鎴栬矾鐢卞彉鏇撮兘搴旂缉灏忚寖鍥村苟淇濈暀鍙洖婊氭簮澶淬€?
