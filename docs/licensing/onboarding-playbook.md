# Onboarding Playbook – PromptOps Lifecycle Governance

This playbook guides teams through the initial onboarding process for adopting PromptOps Lifecycle Governance.

It is designed for:

- Internal platform teams
- SDK PMs
- Infra leads setting up prompt pipelines

---

## Phase 1: Install Core Governance Scaffolds

✅ Clone the repo and install dependencies:

```bash
git clone https://github.com/PromptDeploy/promptops-lifecycle-governance.git
cd promptops-lifecycle-governance
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

✅ Run the full CI test gate:

```bash
make test
```

✅ Review output logs and prompt eval report:

- `evals/eval-report.md`
- `logs/log-sample.output.json`

---

## Phase 2: Role Setup and File Ownership

| Role                | Responsibility                           | File/Workflow                                |
| ------------------- | ---------------------------------------- | -------------------------------------------- |
| Prompt Author       | Writes and submits prompt card           | `schemas/prompt-card.example.yml`            |
| Eval Maintainer     | Owns test cases and thresholds           | `evals/test-cases.json`, `eval-config.*.yml` |
| CI Integrator       | Hooks eval gate into GitHub Actions      | `.github/workflows/ci-prod-block.yml`        |
| Approver (optional) | Signs off manually or via policy-as-code | `policy-as-code-example.yml`                 |
| Logging Owner       | Validates log format and drift checks    | `schemas/prompt-log-schema.json`             |

---

## Phase 3: Integration Rollout

1. **Track Prompt Versions**

   - Use `schemas/prompt-version-schema.yml` to version approved prompts

2. **Gate All Prompt Merges**

   - Enforce `eval-gate.yml` as a PR blocker for unsafe prompts

3. **Implement Approval Flow**

   - Use `policy-as-code-example.yml` or HITL to block unvetted deploys

4. **Start Cost & Drift Logging**

   - Activate `agenttrace-schema.json.json` and monitor changes post-deploy

5. **Promote and Audit**
   - Use `promotion-pipeline.md` to tag and release new prompt versions
   - Monitor `audit/artifact-audit-log.md` for traceability

---

## Recommended Add-ons

| Asset                         | Why It Helps                                        |
| ----------------------------- | --------------------------------------------------- |
| `org-maturity-ladder.md`      | Score internal adoption and maturity                |
| `adoption-checklist.md`       | Track rollout tasks and team readiness              |
| `prompt-lifecycle-diagram.md` | Visually anchor governance logic in onboarding docs |

---

## 💬 Contact

For integration help, fork guidance, or licensing support:  
📧 kappainnovationllc@gmail.com  
🔗 https://linkedin.com/in/houchia
