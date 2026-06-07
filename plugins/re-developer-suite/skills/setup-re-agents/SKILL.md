---
name: setup-re-agents
description: Use when installing, updating, checking, or removing the four RE Developer Suite custom agent templates on a Codex machine.
---

# Setup RE Agents

Use the bundled `scripts/install_agents.py`.

- Default target: `~/.codex/agents`.
- Run `--check` first and report planned creates, updates and unchanged files.
- Install only after the user requested installation.
- Existing different files require `--apply`; the script creates timestamped backups before replacement.
- Never edit global `AGENTS.md`.
- After installation, run `--check` again and advise starting a new Codex thread.

Also verify the user's Codex configuration keeps `agents.max_depth = 1` and `agents.max_threads = 6`. Report the required snippet; do not overwrite unrelated configuration.
