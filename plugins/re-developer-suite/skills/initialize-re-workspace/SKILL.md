---
name: initialize-re-workspace
description: Use when creating or validating a real-estate data workspace for RE Developer Suite without placing deal data inside the plugin.
---

# Initialize RE Workspace

Use `scripts/initialize_workspace.py`.

- Default target is the current working directory.
- Run `--check` before `--apply`.
- Create only missing directories and starter files.
- Never overwrite a non-empty `AGENTS.md` or `re-workspace.yaml`.
- Keep deals, internal knowledge and outputs outside the plugin.
- Explain that local `templates-local/` may override plugin templates by filename when the user explicitly requests that behavior.
