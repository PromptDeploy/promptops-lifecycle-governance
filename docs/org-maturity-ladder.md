# Org Maturity Ladder – PromptOps Lifecycle Adoption

This ladder defines the stages an organization typically moves through as it adopts the PromptOps Lifecycle Governance framework.

Use this to:

- Assess current governance maturity
- Plan rollout phases
- Prioritize onboarding, logging, eval, and promotion adoption

---

## Maturity Stages

| Level | Stage Name      | Description                                                                                   |
| ----- | --------------- | --------------------------------------------------------------------------------------------- |
| 0     | Untracked       | Prompts are manually edited, undocumented, and untested.                                      |
| 1     | Logged          | Prompt inputs/outputs are logged for traceability.                                            |
| 2     | Versioned       | Prompts use semantic versioning and changelogs.                                               |
| 3     | Evaluated       | Prompts are gated by evals before promotion.                                                  |
| 4     | Policy-Governed | Prompt deployment governed by policy-as-code or HITL.                                         |
| 5     | Auditable       | Audit logs, OWASP mappings, and cost telemetry are standard.                                  |
| 6     | Self-Governing  | Teams run full CI/CD lifecycle with rollout templates, dashboards, and compliance checklists. |

---

## How to Use This Ladder

- Run a self-assessment every quarter
- Track adoption across teams or SDK surfaces
- Use this as a planning tool for integration guides and onboarding kits

For deeper integration, see: `onboarding-playbook.md` and `adoption-checklist.md`
