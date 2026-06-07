from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "re-developer-suite"


class BundleTests(unittest.TestCase):
    def test_marketplace_points_to_plugin(self) -> None:
        marketplace = json.loads(
            (ROOT / ".agents" / "plugins" / "marketplace.json").read_text("utf-8")
        )
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], "re-developer-suite")
        self.assertEqual(entry["source"]["path"], "./plugins/re-developer-suite")

    def test_agent_templates_are_valid_and_unpinned(self) -> None:
        paths = sorted((PLUGIN / "agent-templates").glob("*.toml"))
        self.assertEqual(len(paths), 4)
        for path in paths:
            data = tomllib.loads(path.read_text("utf-8"))
            self.assertTrue(data["name"])
            self.assertTrue(data["description"])
            self.assertTrue(data["developer_instructions"])
            self.assertNotIn("model", data)

    def test_full_migration_manifest(self) -> None:
        manifest = json.loads(
            (PLUGIN / "references" / "migration-manifest.json").read_text("utf-8")
        )
        self.assertEqual(manifest["release_target"], "0.2.0")
        self.assertEqual(len(manifest["skills"]), 12)
        self.assertEqual(len(manifest["department_guides"]), 8)
        self.assertTrue(
            all(item["source_exists_at_migration"] for item in manifest["skills"])
        )
        migrated_files = sum(len(item["files"]) for item in manifest["skills"])
        self.assertEqual(migrated_files, 50)

    def test_no_excluded_runtime_artifacts(self) -> None:
        forbidden_suffixes = {".db", ".lock", ".log", ".env"}
        forbidden_names = {
            "memory.md",
            "config.yaml",
            "auth.json",
            "auth.lock",
        }
        for path in PLUGIN.rglob("*"):
            if not path.is_file():
                continue
            self.assertNotIn(path.suffix.lower(), forbidden_suffixes, path)
            self.assertNotIn(path.name.lower(), forbidden_names, path)
            self.assertFalse(
                {part.lower() for part in path.parts}.intersection(
                    {"sessions", "cache", "logs", "memories"}
                ),
                path,
            )

    def test_agent_installer_creates_and_backs_up(self) -> None:
        script = PLUGIN / "scripts" / "install_agents.py"
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "agents"
            check = subprocess.run(
                [sys.executable, str(script), "--check", "--target", str(target)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("CREATE", check.stdout)
            subprocess.run(
                [sys.executable, str(script), "--apply", "--target", str(target)],
                check=True,
                capture_output=True,
                text=True,
            )
            changed = target / "re-legal.toml"
            changed.write_text("# local override\nname='local'\n", encoding="utf-8")
            subprocess.run(
                [sys.executable, str(script), "--apply", "--target", str(target)],
                check=True,
                capture_output=True,
                text=True,
            )
            backups = list((target / "backups").rglob("re-legal.toml"))
            self.assertEqual(len(backups), 1)
            self.assertIn("local override", backups[0].read_text("utf-8"))

    def test_workspace_initializer_preserves_existing_agents(self) -> None:
        script = PLUGIN / "scripts" / "initialize_workspace.py"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            agents = root / "AGENTS.md"
            agents.write_text("# Existing\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), "--apply", "--target", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PRESERVE", result.stdout)
            self.assertEqual(agents.read_text("utf-8"), "# Existing\n")
            self.assertTrue((root / "deals").is_dir())
            self.assertTrue((root / "re-workspace.yaml").is_file())


if __name__ == "__main__":
    unittest.main()
