# Adoption Checklist Audit: Track Governance Implementation Progress

This checklist helps teams track their rollout progress of the PromptOps Lifecycle Governance framework.

Use it for:

- Governance self-assessment
- Team onboarding readiness
- Licensing and acquirer prep

## Core Infrastructure

- [ ] Repo cloned and installed (`make test` runs cleanly)
- [ ] Python + Promptfoo dependencies installed
- [ ] Logs and test reports reviewed (`evals/eval-report.md`, `logs/`)

## Prompt Governance Setup

- [ ] Prompt cards structured (`schemas/prompt-card.example.yml`)
- [ ] Prompt version schema applied (`schemas/prompt-version-schema.yml`)
- [ ] Changelog format in use (`schemas/prompt-change-log.yml`)
- [ ] Prompt eval config loaded (`evals/eval-config.promptfoo.yml`)

## Evaluation & CI/CD Gating

- [ ] Thresholds defined (`eval-config.promptfoo.yml`)
- [ ] Eval pass/fail logic enforced (`ci/eval-gate.yml`)
- [ ] GitHub Action blocking unapproved prompt merges
- [ ] Prompt regression test case defined (`tests/prompt-regression.test.json`)

---

## Approval & Policy Control

- [ ] Policy-as-code configured (`policy-as-code-example.yml`)
- [ ] HITL approval step documented or implemented
- [ ] Promotion process mapped (`promotion-pipeline.md`)

---

## Logging & Auditability

- [ ] Logs structured to match schema (`log-schema-v2.json`)
- [ ] Cost and drift monitoring activated (`logs/`, `cost-checks.yml`)
- [ ] Agent logging traced per step (`agent-log.example.json`)

---

## Compliance Mapping

- [ ] OWASP LLM checklist mapped (`owasp-llm-checklist.md`)
- [ ] Artifact audit log maintained (`artifact-audit-log.md`)
- [ ] Failure modes catalog reviewed (`failure-modes-catalog.md`)
- [ ] Standards alignment confirmed (`compliance-mapping.md`)

## Organizational Adoption

- [ ] Org maturity ladder reviewed (`org-maturity-ladder.md`)
- [ ] Onboarding playbook distributed (`onboarding-playbook.md`)
- [ ] This checklist reviewed quarterly

## Internal Contact

| Role          | Name / Slack / Email |
| ------------- | -------------------- |
| Prompt Author |                      |
| CI Maintainer |                      |
| Logging Owner |                      |
| SDK PM        |                      |
