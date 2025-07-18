# CHANGELOG

All notable changes to the PromptOps Lifecycle Governance artifact will be documented here.

---

## v0.1.0 – Initial Release

Date: 2025-07-14  
Commit Hash: _To be added after initial public push_
Author: Hou Chia

### Features

- Prompt versioning schemas (`prompt-version-schema.yml`, `prompt-card.example.yml`)
- Prompt evaluation pipeline with Promptfoo (`evalsuite-core-config.yml`, `test-cases.json`)
- Cost telemetry logging + schema (`prompt-log-schema.json`, `cost-metrics-schema.yml`)
- CI gating for eval regressions (`eval-gate.yml`, `check_eval_thresholds.py`)
- Human-in-the-loop approval process (`HITL_Approval_Template.md`)
- Prompt injection test suite and rollback conditions
- Sample agent orchestration, OpenAPI, and Pinecone integration guides

### Governance Pillars Covered

- PromptOps Lifecycle
- Evaluation Governance
- Cost-Risk-ROI
- Agent Orchestration
- Prompt Safety (partial)

## v0.2.0 – Documentation Refactor & Role-Based Indexing

Date: 2025-07-16  
Commit Hash: _To be added on merge_
Author: Hou Chia

### Improvements

- Introduced structured `/docs/` system with role-based folders:
  - `getting-started/`, `implementation/`, `governance/`, `licensing/`
- Moved tutorial files into implementation docs (`promptops-lifecycle-trace.md`)
- Created central index at `docs/index.md` with audience-specific navigation
- Cleaned up `examples/` to avoid overlap with `/docs/` and reflect canonical usage
- Updated `README.md` to reflect doc structure and roles
- Aligned folder structure more clearly with governance pillars and licensing readiness

### Vault Metadata

- Vault Packaging bumped to: `v0.2.0`
- Governance Pillars Clarified:
  - PromptOps Lifecycle
  - Evaluation Governance
  - Cost-Risk-ROI
  - Agent Governance
  - Promotion + Rollback
  - Audit Readiness
