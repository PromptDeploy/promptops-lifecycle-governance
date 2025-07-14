# CHANGELOG

All notable changes to the PromptOps Lifecycle Governance artifact will be documented here.

---

## v0.1.0 – Initial Release

Date: 2025-07-14  
Commit Hash: _To be added after initial public push_
Author: Hou Chia

### Features

- Prompt versioning schemas (`prompt-version-schema.yml`, `prompt-card.example.yml`)
- Prompt evaluation pipeline with Promptfoo (`eval-config.promptfoo.yml`, `test-cases.json`)
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
