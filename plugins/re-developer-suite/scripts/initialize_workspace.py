#!/usr/bin/env python3
"""Create a minimal RE data workspace without overwriting existing content."""

from __future__ import annotations

import argparse
from pathlib import Path


DIRECTORIES = (
    "deals",
    "knowledge/shared",
    "knowledge/departments/legal",
    "knowledge/departments/investment-finance",
    "knowledge/departments/market-research",
    "knowledge/departments/project-design",
    "templates-local",
    "outputs",
)

STARTER_FILES = {
    "AGENTS.md": """# Real Estate Workspace

## Working rules

- Use the installed RE Developer Suite workflows for real-estate tasks.
- Speak Vietnamese by default, refer to the user as Sếp and yourself as em.
- Keep deal-specific facts in `deals/<deal-id>/`.
- Keep durable internal knowledge under `knowledge/`.
- Distinguish confirmed facts, inferences, assumptions and unresolved items.
- Do not send private workspace content to external tools without explicit approval.
- For cross-functional work, use RE-HQ; for specialist work, use the matching RE agent.
""",
    "re-workspace.yaml": """schema_version: 1
workspace_type: real-estate-developer
default_language: vi
data_policy:
  external_upload_requires_approval: true
paths:
  deals: deals
  shared_knowledge: knowledge/shared
  department_knowledge: knowledge/departments
  local_templates: templates-local
  outputs: outputs
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--target", type=Path, default=Path.cwd())
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.target.expanduser().resolve()
    actions: list[tuple[str, Path, str | None]] = []

    for relative in DIRECTORIES:
        path = root / relative
        actions.append(("UNCHANGED" if path.is_dir() else "CREATE_DIR", path, None))

    for relative, content in STARTER_FILES.items():
        path = root / relative
        if not path.exists():
            action = "CREATE_FILE"
        elif path.read_text(encoding="utf-8").strip():
            action = "PRESERVE"
        else:
            action = "CREATE_FILE"
        actions.append((action, path, content))

    for action, path, _ in actions:
        print(f"{action:11} {path}")

    if args.check:
        return 0

    root.mkdir(parents=True, exist_ok=True)
    for action, path, content in actions:
        if action == "CREATE_DIR":
            path.mkdir(parents=True, exist_ok=True)
        elif action == "CREATE_FILE":
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content or "", encoding="utf-8", newline="\n")

    print(f"Workspace ready: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
