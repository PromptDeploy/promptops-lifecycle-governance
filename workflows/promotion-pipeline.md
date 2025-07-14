# Prompt Promotion Pipeline

This document outlines the governance-compliant pipeline for promoting prompt artifacts from development to staging to production inside SaaS SDK systems.

## Promotion Stages

1. **Author & Draft Prompt**

   - Create the raw system prompt or prompt chain.
   - Wrap in governance metadata via `schemas/prompt-card.example.yml`.

2. **Apply Versioning**

   - Assign version, hash, author, and environment via `schemas/prompt-version-schema.yml`.

3. **Evaluation Gate**

   - Run prompt through reproducible evals:
     - Accuracy / Hallucination tests
     - Cost and token checks
     - Safety/PII leakage checks
   - Defined in `evals/eval-config.promptfoo.yml`, enforced via `ci/eval-gate.yml`.

4. **Log Trace & Metadata**

   - Capture trace fields, inputs, outputs, model, context:
     - `logs/prompt-log-schema.json`
     - `logs/log-sample.output.json`

5. **Approval Gate**

   - One of:

     - Manual human approval using [`HITL_Approval_Template.md`](./HITL_Approval_Template.md)
     - Policy-as-code check via `workflows/policy-as-code-example.yml`

   - If human-in-the-loop (HITL) is required:
     - Reviewer must complete and store the HITL form in `/reviews/`
     - Form must be included in changelog PR before promotion
     - Reviewer roles: PM, Tech Lead, QA, Security, Governance

6. **Promotion Trigger**

   - If all gates pass, prompt can be:
     - Merged to `main` or `production` branch
     - Registered in SDK registry (e.g., config file, db table)
     - Marked with `environment: prod` and added to change log

7. **Audit Trail Update**
   - Append to:
     - `schemas/prompt-change-log.yml`
     - `audit/artifact-audit-log.md`

---

## Promotion Checklist

| Requirement                       | File Location                                                         |
| --------------------------------- | --------------------------------------------------------------------- |
| Prompt metadata attached          | `schemas/prompt-card.example.yml`                                     |
| Version and hash assigned         | `schemas/prompt-version-schema.yml`                                   |
| Eval tests passed                 | `evals/eval-config.promptfoo.yml`                                     |
| Eval CI passed                    | `ci/eval-gate.yml`                                                    |
| Trace log created                 | `logs/log-sample.output.json`                                         |
| Approval granted or policy passed | `HITL_Approval_Template.md` or `workflows/policy-as-code-example.yml` |
| Changelog updated                 | `schemas/prompt-change-log.yml`                                       |

---

## Rollback Instructions

If promotion fails post-deployment:

- Reference `workflows/rollback-flow.md`
- Revert to last passing version
- Notify stakeholders
- Re-run evals for updated prompt

---

## Summary

This pipeline ensures that every prompt promoted to production meets governance, safety, and reproducibility standards. It’s optimized for teams that need to balance velocity with trust.
