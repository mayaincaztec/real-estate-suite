# RE Developer Suite Marketplace

Private Codex marketplace for a Vietnamese real-estate developer operating model.

## Included

- RE-HQ coordination and routing
- RE-Legal
- RE-Investment-Finance
- RE-Market-Research
- RE-Project-Design
- Due diligence and deal-structuring workflows
- Safe custom-agent installer and data-workspace initializer

The plugin contains workflows and templates only. Keep deal documents, internal
knowledge, credentials and generated outputs in a separate data workspace.

## Install From Private GitHub

```powershell
codex plugin marketplace add mayaincaztec/re-developer --ref v0.2.0 --sparse .agents/plugins --sparse plugins
codex plugin add re-developer-suite@re-developer-suite-private
```

Start a new thread, invoke `setup-re-agents`, then invoke
`initialize-re-workspace` from the intended data workspace.

Private Git authentication must already work on the machine. Prefer the
organization's approved credential manager or SSH policy; do not store tokens
inside this repository.

## Pilot And Promotion

1. Tag a semantic version such as `v0.2.0`.
2. Install that tag on the personal pilot machine.
3. Run the checks in `tests/ACCEPTANCE.md`.
4. Promote the same immutable tag to the company machine.
5. Do not use `main` as a production installation source.

## Upgrade

Upgrade the marketplace snapshot to an approved tag, reinstall the plugin, open
a new thread, and run `setup-re-agents` in check mode before applying agent
template updates.

```powershell
codex plugin marketplace upgrade re-developer-suite-private
codex plugin add re-developer-suite@re-developer-suite-private
```

## Development Checks

Run from the repository root with Python 3.11+:

```powershell
python plugins/re-developer-suite/scripts/check_bundle.py
python -m unittest discover -s tests -v
```

Validate the plugin with Codex's `plugin-creator` validator before release.

## Migrated Business Library

Version `0.2.0` contains the complete selected business library from the prior
profiles: 12 detailed skills containing 50 files, their references, legal
templates, checklists, DD and structuring workflows, plus eight department
operating/library guides.

The migration intentionally excludes memories, sessions, cache, logs,
databases, model configuration, authentication, runtime files and `.env`
files. See `plugins/re-developer-suite/references/migration-manifest.json`.
