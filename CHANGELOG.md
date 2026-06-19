# Changelog

## 0.10.0 - 2026-06-20

### re-legal-counsel upgrade — integrate corporate-legal (Claude for Legal) methodology
Reviewed Anthropic's `corporate-legal` plugin (github.com/anthropics/claude-for-legal) and integrated the parts that fit a specialist contract/transaction lawyer, adapted to Vietnamese RE/M&A. Coordination-only skills (closing-checklist, deal-team-summary, integration-management, entity-compliance, dataroom-watcher) were deliberately NOT integrated — those stay with `re-inv` (deal lifecycle owner); AI-tool-handoff and plugin infra were out of scope.

- New references under `re-legal-counsel`: `transaction-dd-playbook.md` (document-set legal DD adapted from diligence-issue-extraction + tabular-review — issue categories, materiality, 4-level severity, finding format, source attribution via tvpl), `transaction-clause-checklists.md` (change-of-control / assignment / MAC / MFN / indemnity / termination / CP / successor-liability), `corporate-approvals-vn.md` (board/shareholder resolutions & minutes under Luật Doanh nghiệp 2020, with conflict-of-interest and major-action gates).
- `re-legal-counsel` SKILL: added Mode 4 (transaction legal DD on a document set) and Mode 5 (drafting corporate approval instruments); enriched contract-review with the clause taxonomy and tabular review; new output shapes; broadened description.
- New templates: `transaction-dd-findings-memo`, `clause-review-grid`, `material-contract-schedule`, `corporate-resolution-vn`.
- Boundary kept clean: project-legal DD (land/zoning/permits) defers to `re-legal-licensing`; DD coordination defers to `re-inv-dd-coordinator` (which now points to the playbook); CP/closing actions hand off to cp-closing-issue-note.
- Anti-drift sync: `re-legal-operations` matrix + template map and `re-legal-verification-rules` (new deliverable checks J/K/L) updated; link-integrity and bundle tests green.

## 0.9.0 - 2026-06-11

### Department-prefix renaming (22 → 21 skills)
- Renamed all skills to carry their department prefix; each department entry skill now matches its agent name: `re-rnd` (market research / R&D), `re-inv` (investment), `re-legal` (unchanged), `re-project` (project & design). `re-hq` and `initialize-re-workspace` stay unprefixed (shared).
- `vn-re-research` → `re-rnd`; the thin `re-market-research` entry merged into it (department role, source rules, output checklist absorbed) — owner picked `re-rnd` over the requested `re-r&d` because `&` violates the Claude Code skill-name spec.
- Investment: `re-investment-finance` → `re-inv`; `re-investment-screening` → `re-inv-screening`; `re-preliminary-investment-report` → `re-inv-preliminary-report`; `re-feasibility-study` → `re-inv-feasibility-study`; `re-full-investment-report` → `re-inv-full-report`; `deal-structuring-advisor` → `re-inv-deal-structuring`; `dd-coordinator` → `re-inv-dd-coordinator`; operating-matrix and verification-rules follow the prefix.
- Legal: `licensing-expert` → `re-legal-licensing`; `legal-counsel` → `re-legal-counsel`; `legal-writing` → `re-legal-writing`; `doc-renamer` → `re-legal-doc-renamer`.
- Project & design: `re-project-design` → `re-project`; `design-planning` → `re-project-design-planning`.
- Agents renamed to match: `re-rnd`, `re-inv`, `re-project` (re-legal unchanged). All cross-references updated across skills, references, templates, agents, commands, scripts, README; naming convention codified in `skill-authoring-guide.md`; link-integrity and bundle tests green.

## 0.8.0 - 2026-06-11

### vn-re-research overhaul (market-research engine)
- Rewrote `vn-re-research` (v2.0.0): dropped the legacy OpenClaw migration header, English trigger description, Vietnamese headers; SKILL.md now holds only SOP — 6 protocols: P1 add/update project, P2 price update, P3 reports, P4 weekly/monthly scan, P5 field audit (new, codified from vault practice), P6 taxonomy/schema ops via review-first manifests (new).
- Split domain knowledge into 4 references: `vault-layout.md` (vault data contract incl. district/cluster folder convention and vault↔skill sync rules), `project-data-spec.md` (frontmatter rules, taxonomy v2, do_chinh_xac thresholds, field priorities, segment table with as-of), `pricing-protocol.md` (unit-of-analysis ladder, 4 price types, anchor-vs-average — generalized from the Nhon Trach pricing playbook), `report-catalog.md`.
- P2 rewritten to follow the pricing protocol: choose unit of analysis first, body tables (5A–5E) hold the detail, frontmatter `gia_tb_*` only when a common baseline is valid.
- Added 8 market-research report templates under `templates/market-research/`: market-snapshot, area-study, price-comparison-ranking, weekly-scan, monthly-market-report, pricing-playbook, field-audit, phase-sheet.
- Wired the vault path into `re-workspace.yaml` (`market_research_vault` key, seeded by the initializer); updated `workspace-layout.md` and `re-market-research` accordingly.
- Vault-side cleanup (outside repo): added `_config/taxonomy/geo-mapping.md` (market zones vs post-merger 2025 admin units), `_config/QUERIES/05-stale-data.md` (90-day price staleness + missing-MBS queries), reorganized `reports/` (playbooks/, field-audits/, phase-sheets/), template v2.3 (`don_vi_hanh_chinh_2025` field, fixed BRVT/VTU code mismatch), repointed `AGENT_SKILL.md` to the plugin, removed `.openclawignore`.
- Deferred per owner request: section E expansion scopes (supply pipeline, launch monitoring, rental/yield, developer profiling…).

## 0.7.0 - 2026-06-11

### Legal bundle consolidation (25 → 22 skills)
- Merged the three overlapping RE-Legal meta layers (`re-legal-intake-router`, `re-legal-operating-matrix`, `re-legal-deliverable-templates`) into a single operations layer `re-legal-operations` (intake → matrix → template map). Routing now lives in one place per department; updated every referencing skill and guide.
- Removed `re-legal-skill-maintenance` (legacy-runtime maintenance utility); the still-relevant content (backup-before-sync, verify-after-sync, anti-drift checklist, quarterly static-knowledge re-verification cadence) moved into `references/skill-authoring-guide.md` as maintainer docs. Deleted the redundant `department-guides/re-legal-library-readme.md` (third copy of the matrix).
- Fixed routing drift: `licensing-expert` and the legal operating guide no longer route DD coordination / multi-stream work to RE-HQ — deal-lifecycle coordination routes to RE-Investment-Finance per `routing-map.md`; RE-HQ only for executive synthesis.

### Deal dossier & workspace layout
- New `templates/deal-dossier.md` — living per-deal state file (`deals/<deal-id>/_dossier.md`): lifecycle status, assumption register, findings, decisions, open questions, session log. All deal-lifecycle skills (screening, preliminary, FS, full/IC, structuring, DD) now read it at session start and update it at session end.
- New `references/workspace-layout.md` — single source of truth for the data-workspace structure and output naming; `initialize_workspace.py` CLAUDE.md starter now points to it.

### Commands & agents
- New `commands/`: `/re-screen`, `/re-fs`, `/re-dd`, `/re-status` for deterministic entry into the deal workflows.
- New `agents/`: four department agents (`re-legal`, `re-market-research`, `re-project-design`, `re-investment-finance`) with scoped tools for parallel workstreams via the Agent tool; wired into `routing-map.md`.

### Quality & domain hygiene
- Verification trace rule in `operating-contract.md`: official deliverables must end with the "Kiểm tra trước khi chốt" block (or log it in the deal dossier); wired into both verification skills.
- English-description rule enforced: rewrote 8 mixed-language skill descriptions to English (Vietnamese glosses allowed); `check_bundle.py` now lints descriptions and forbidden English section headers, and `tests` run it as a test case.
- Static-knowledge dating: renamed `vn-legal-texts-2025.md` → `vn-legal-texts.md` and `agencies-and-authority-2025.md` → `agencies-and-authority.md`; added explicit `as-of` lines to these and `structuring-tax-guide.md`, tied to the quarterly re-verification cadence in the authoring guide.
- README: corrected structure diagram (tests live at repo root), documented the deliberate scope boundary (post-investment phases out of scope for now).
- Deferred per owner request: `vn-re-research` content update (incl. post-merger province taxonomy) and the VN finance-norms reference.

## 0.6.0 - 2026-06-08

- Merged superior content from the user's standalone skills into the plugin (dropping legacy "OpenClaw" branding, keeping tvpl/routing): `licensing-expert` gains `references/agencies-and-authority-2025.md` (post-merger agencies, 2-level local government from 01/07/2025, citation order) and a 4-level risk scale (🔴🟠🟡🟢) in the legal-status report template; `legal-counsel` gains `references/negotiation-and-dispute-playbook.md` (issue tiers, 3-round negotiation, dispute-resolution comparison, statute of limitations, arbitration).
- Vietnamese-principle audit: localized 125 English section headers and inline labels to Vietnamese across 22 skills (When to Use → Khi nào dùng, Workflow → Quy trình, Overview → Tổng quan, etc.); skill name/description stay English for triggering. Codified the header rule in `skill-authoring-guide.md`.
- English-deliverable support: added an Output-language rule to `operating-contract.md` (working language Vietnamese; deliverable language follows the user's request or governing context — e.g. English-form contract → English memo), wired into `legal-writing`, `legal-counsel`, and the authoring guide.

## 0.5.0 - 2026-06-08

- Unified template location: moved the 14 legal deliverable templates from `re-legal-deliverable-templates/references/` to the shared `templates/`; that skill now selects/points to `../../templates/...`. Convention (documented in `skill-authoring-guide.md`): deliverables live in `templates/`, only technical specs/guides live in a skill's `references/`.
- Strengthened RE-HQ for its arbitration/synthesis role: added a conflict-arbitration checklist and `templates/integrated-decision-memo.md`.
- Documented the naming convention + grandfather rule in `skill-authoring-guide.md`.

## 0.4.0 - 2026-06-08

- Removed all legacy Codex runtime artifacts: `agent-templates/*.toml`, `scripts/install_agents.py`, and the `setup-re-agents` skill. On Claude the departments are skills with no agent-install step.
- `initialize_workspace.py` now seeds `CLAUDE.md` (was `AGENTS.md`); updated the `initialize-re-workspace` skill and tests accordingly.
- Refreshed `check_bundle.py` (dropped agent-template validation), tests, README and `ACCEPTANCE.md` to the current 25-skill Claude bundle.
- Added an Excel prerequisite note (xlsx/openpyxl) to `re-feasibility-study`.
- Added `references/skill-authoring-guide.md` codifying suite conventions (frontmatter, language, references/link-integrity, routing ownership, naming, add/remove checklist).

## 0.3.1 - 2026-06-08

- Added `re-investment-operating-matrix` to standardize the RE-Investment-Finance bundle (task → skill → specialist pull → template → verification → escalation), at parity with the legal operating matrix.
- Added `test_internal_md_references_resolve` — a link-integrity test that verifies every intra-bundle relative reference (`../...md`, `references/...md`) resolves; fixed the broken/loose references it surfaced (re-hq, setup-re-agents, doc-renamer, tvpl-lookup-protocol, loi-and-offer-guide).
- Removed leftover empty `skills/deal-structuring/` directory.

## 0.3.0 - 2026-06-08

### Runtime cleanup & coherence
- Removed Codex residue across skills; pointed browser workflows to Claude in Chrome / WebFetch.
- Reframed `setup-re-agents` as legacy/compat (no agent install on Claude); fixed stale `check_bundle.py` and `tests/test_bundle.py` paths.
- Consolidated routing into a single source of truth (`references/routing-map.md`); trimmed duplicated routing in operating guides.
- Removed redundant `deal-structuring` skill; synced version/license frontmatter across all skills; removed the one-time `migration-manifest.json` and its test.

### tvpl legal integration
- Added `references/tvpl-lookup-protocol.md` and wired MCP `tvpl` (search / check_hieu_luc / get_dieu / get_luoc_do / so_sanh_dieu) into `licensing-expert`, `legal-counsel`, and `re-legal-verification-rules` for live legal-text and effect verification.

### RE-Investment-Finance — full deal lifecycle bundle
- `re-investment-finance` now owns the deal lifecycle. New skills: `re-investment-screening`, `re-preliminary-investment-report`, `re-feasibility-study` (spec + Excel generator), `re-full-investment-report`, `re-investment-verification-rules`.
- Moved `dd-coordinator` and `deal-structuring-advisor` (with FS→offer→LOI) from RE-HQ to RE-Investment-Finance; RE-HQ now executive-synthesis only. New templates: deal-screening-note, preliminary/full investment report, LOI.

### RE-Project-Design — design-planning specialist
- Added `design-planning` (1/500 planning-indicator calc engine + 9-step process + QCVN compliance + design review) with calculation-engine and standards references.

### Completed earlier
- Completed RE-Market-Research (engine `vn-re-research` wired in, verification checklist).

## 0.2.1 - 2026-06-07

- Ported the suite to the Claude Code / Cowork plugin standard.
- Added `.claude-plugin/marketplace.json` (repo root) and
  `plugins/re-developer-suite/.claude-plugin/plugin.json`.
- Removed Codex-only manifests (`.agents/plugins/marketplace.json`,
  `.codex-plugin/plugin.json`). Skills, references and templates unchanged.
- Rewrote README install instructions for `/plugin marketplace add` + `/plugin install`.

## 0.2.0 - 2026-06-07

- Migrated the complete selected legal reference, template and checklist library.
- Added detailed DD, deal structuring, legal intake, licensing, legal counsel,
  legal writing, document operations, quality-control and VN market workflows.
- Added all department operating guides and the cross-profile routing playbook.
- Normalized legacy runtime paths and tool instructions for Codex.
- Added a migration coverage manifest and hard exclusions for memory, sessions,
  cache, logs, databases, model configuration, authentication, runtime files
  and `.env` files.

## 0.1.0 - 2026-06-07

- Added the private Codex marketplace and `re-developer-suite` plugin.
- Added RE-HQ and four departmental workflow skills.
- Added DD and deal-structuring coordination workflows.
- Added four versioned custom-agent templates.
- Added safe agent installation and workspace initialization scripts.
- Added shared finding, handoff, DD, investment, market and design templates.
- Added static bundle checks and acceptance tests.

Migration note: Hermes/OpenClaw runtime configuration, caches, logs, memories,
sessions and credentials are intentionally excluded. Historical legal and tax
references must be re-verified against current primary sources.
