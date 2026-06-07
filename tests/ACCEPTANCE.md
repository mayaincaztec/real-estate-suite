# Acceptance Checklist

## Static

- Plugin manifest passes the Codex plugin validator.
- Marketplace resolves `./plugins/re-developer-suite`.
- Nine skills are discovered.
- Four agent templates parse as TOML and do not pin a model.
- Bundle contains no credentials, databases, logs or deal folders.

## Personal Pilot

- Install the marketplace from an immutable release tag.
- Install the plugin and start a new thread.
- Run `setup-re-agents` check, apply and re-check.
- Confirm all four custom agent names are available in a new thread.
- Initialize a temporary RE workspace and confirm existing files are preserved.
- Run one task for each department.
- Run one ambiguous routing task through RE-HQ.
- Run a simulated DD using at least Legal, Investment & Finance and Market Research.
- Confirm outputs distinguish confirmed, inferred, assumed and unresolved items.
- Confirm current web sources include links and access dates.

## Company Promotion

- Install the same tested tag, not `main`.
- Repeat plugin and agent discovery checks.
- Confirm company permissions allow private marketplace installation.
- Confirm no private workspace content is sent externally without approval.
- Record installed plugin and agent-template version.
