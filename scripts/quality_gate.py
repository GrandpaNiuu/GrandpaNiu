#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys

COMMANDS = [
    [sys.executable, "scripts/build_android_rules.py"],
    [sys.executable, "scripts/build_module.py", "--build", "--profile", "fusion"],
    [sys.executable, "scripts/factory_finalize.py", "--sync-root"],
    [sys.executable, "scripts/build_release_variants.py"],
    [sys.executable, "scripts/validate_repository.py"],
]


def main() -> None:
    for command in COMMANDS:
        print("$ " + " ".join(command), flush=True)
        subprocess.run(command, check=True)
    print("Quality gate passed.")


if __name__ == "__main__":
    main()
