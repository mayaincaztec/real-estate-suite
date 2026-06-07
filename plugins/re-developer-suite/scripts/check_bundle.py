#!/usr/bin/env python3
"""Static checks for the RE Developer Suite bundle."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = 0

    manifest = json.loads((root / ".codex-plugin" / "plugin.json").read_text("utf-8"))
    if manifest.get("name") != root.name:
        fail("plugin folder and manifest name differ")
        errors += 1

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    expected_skills = {
        "re-hq",
        "setup-re-agents",
        "initialize-re-workspace",
        "dd-coordinator",
        "deal-structuring",
        "deal-structuring-advisor",
        "doc-renamer",
        "legal-counsel",
        "legal-writing",
        "licensing-expert",
        "re-legal",
        "re-legal-deliverable-templates",
        "re-legal-intake-router",
        "re-legal-operating-matrix",
        "re-legal-skill-maintenance",
        "re-legal-verification-rules",
        "re-investment-finance",
        "re-market-research",
        "re-project-design",
        "vn-re-research",
    }
    if {path.parent.name for path in skills} != expected_skills:
        fail("skill set does not match expected v1 bundle")
        errors += 1

    for path in skills:
        text = path.read_text("utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            fail(f"invalid skill frontmatter: {path}")
            errors += 1
        lowered = text.lower()
        for forbidden in ("profile=\"chrome-relay\"", "~/.openclaw", "hermes-native"):
            if forbidden in lowered:
                fail(f"legacy runtime reference in {path}: {forbidden}")
                errors += 1

    for path in sorted((root / "agent-templates").glob("*.toml")):
        data = tomllib.loads(path.read_text("utf-8"))
        for key in ("name", "description", "developer_instructions"):
            if not data.get(key):
                fail(f"{path} missing {key}")
                errors += 1
        if "model" in data:
            fail(f"{path} pins a model instead of inheriting")
            errors += 1

    forbidden_suffixes = {".db", ".lock", ".log", ".env"}
    forbidden_names = {
        "memory.md",
        "config.yaml",
        "auth.json",
        "auth.lock",
        "models_dev_cache.json",
        "provider_models_cache.json",
        "ollama_cloud_models_cache.json",
        "context_length_cache.yaml",
    }
    for path in root.rglob("*"):
        if path.is_file():
            if path.suffix.lower() in forbidden_suffixes or path.name.lower() in forbidden_names:
                fail(f"forbidden runtime artifact: {path}")
                errors += 1
            lowered_parts = {part.lower() for part in path.parts}
            if lowered_parts.intersection({"sessions", "cache", "logs", "memories"}):
                fail(f"forbidden runtime directory content: {path}")
                errors += 1

    if errors:
        print(f"Bundle check failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(f"Bundle check passed: {len(skills)} skills, 4 agent templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
