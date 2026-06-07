#!/usr/bin/env python3
"""Install RE Developer Suite custom agents without silent overwrites."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import sys
import tomllib
from pathlib import Path


AGENT_NAMES = (
    "re-legal.toml",
    "re-investment-finance.toml",
    "re-market-research.toml",
    "re-project-design.toml",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def status(source: Path, target: Path) -> str:
    if not target.exists():
        return "CREATE"
    return "UNCHANGED" if digest(source) == digest(target) else "UPDATE"


def version(path: Path) -> str:
    if not path.exists():
        return "-"
    match = re.search(
        r'^# re-developer-suite-version = "([^"]+)"',
        path.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    return match.group(1) if match else "unversioned"


def validate_agent(path: Path) -> None:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    missing = [
        key
        for key in ("name", "description", "developer_instructions")
        if not data.get(key)
    ]
    if missing:
        raise ValueError(f"{path} missing required keys: {', '.join(missing)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Show planned changes only.")
    mode.add_argument("--apply", action="store_true", help="Install or update templates.")
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.home() / ".codex" / "agents",
        help="Custom agent directory. Defaults to ~/.codex/agents.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    plugin_root = Path(__file__).resolve().parent.parent
    source_dir = plugin_root / "agent-templates"
    target_dir = args.target.expanduser().resolve()
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    planned = []

    for name in AGENT_NAMES:
        source = source_dir / name
        if not source.is_file():
            print(f"ERROR missing template: {source}", file=sys.stderr)
            return 2
        try:
            validate_agent(source)
        except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
            print(f"ERROR invalid template: {exc}", file=sys.stderr)
            return 2
        target = target_dir / name
        planned.append((status(source, target), source, target))

    for action, source, target in planned:
        print(
            f"{action:9} {target} "
            f"(installed={version(target)}, available={version(source)})"
        )

    if args.check:
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)
    backup_dir = target_dir / "backups" / timestamp
    changed = 0

    for action, source, target in planned:
        if action == "UNCHANGED":
            continue
        if action == "UPDATE":
            backup_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup_dir / target.name)
        shutil.copy2(source, target)
        if digest(source) != digest(target):
            print(f"ERROR post-install verification failed: {target}", file=sys.stderr)
            return 3
        changed += 1

    print(f"Installed {changed} changed agent file(s) in {target_dir}")
    if backup_dir.exists():
        print(f"Backups: {backup_dir}")
    print("Recommended Codex config:")
    print("[agents]")
    print("max_threads = 6")
    print("max_depth = 1")
    print("Start a new Codex thread to load the agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
