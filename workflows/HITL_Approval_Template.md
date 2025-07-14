# Human-in-the-Loop (HITL) Approval Template

Use this checklist before promoting a prompt to staging or production. Required for all prompts marked as `status: draft`, `experimental`, or `modified`.

---

## Prompt Metadata

- **Prompt Name / ID**: `__________`
- **Version**: `vX.Y.Z`
- **Environment**: `staging | production`
- **Reviewer(s)**: `__________`
- **Review Date**: `YYYY-MM-DD`
- **Reviewer Role(s)**: `PM | Tech Lead | Security | QA | Governance`

---

## Prompt Change Summary

> What changed in this version (compared to previous)?
>
> - Updated instructions / tone / fallback logic?
> - New inputs or output format?

[ Paste a diff or markdown summary of changes here ]

---

## Evaluation Gate Review

- [ ] All eval tests passed via Promptfoo
- [ ] Pass rate ≥ 90% and avg score ≥ 0.85
- [ ] New test cases added (if new behavior introduced)
- [ ] Cost plugin thresholds not exceeded

---

## Risk & Safety Review

- [ ] Prompt is free of prompt injection risks
- [ ] Sensitive use cases validated (PII, hallucination, compliance)
- [ ] Fallback + rollback paths are clearly defined

---

## Promotion Decision

- [ ] Approved for Promotion to **Staging**
- [ ] Approved for Promotion to **Production**
- [ ] Rejected — requires rework
- [ ] Needs additional stakeholder review

---

## Reviewer Notes

> Any context on rationale, caution flags, mitigation steps, or logs reviewed?

---

## Suggested File Path

Store this as: `/reviews/HITL_logs/{prompt_name}\_vX.Y.Z_approval.md`

---

## Notes

- Required for all prompts with external user impact, LLM model switch, or behavior change.
- Suggested to link to this in `promotion-pipeline.md` and reference in CI (manual gate).
