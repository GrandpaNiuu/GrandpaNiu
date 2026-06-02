#!/usr/bin/env python3
from __future__ import annotations

import subprocess

COMMANDS = [
    ["python3", "scripts/build_android_rules.py"],
    ["python3", "scripts/build_module.py", "--build", "--profile", "stable"],
    ["python3", "scripts/factory_finalize.py", "--sync-root"],
    ["python3", "scripts/build_release_variants.py"],
    ["python3", "scripts/validate_repository.py"],
]


def main() -> None:
    for command in COMMANDS:
        print("$ " + " ".join(command), flush=True)
        subprocess.run(command, check=True)
    print("Quality gate passed.")


if __name__ == "__main__":
    main()
