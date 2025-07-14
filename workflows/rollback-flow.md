# Prompt Rollback Flow

This document outlines the governance-safe procedure for rolling back a prompt artifact after a failed deployment, regression, or drift event.

## Rollback Triggers

You should initiate a rollback if any of the following occur post-promotion:

- Prompt evaluation regressions detected (e.g., accuracy drop, cost spike)
- Drift detected (model behavior changes due to upstream LLM update)
- Failing tests or promptfoo cases after release
- User or stakeholder complaint (e.g., hallucinations, unsafe output)
- Audit review flags prompt anomaly

---

## Rollback Procedure

1. **Locate Last Known Good Version**

   - Find the most recent version that passed all evals and was production-approved.
   - Reference:
     - `schemas/prompt-version-schema.yml`
     - `schemas/prompt-change-log.yml`
     - `logs/log-sample.output.json`

2. **Restore Prompt Artifacts**

   - Checkout the prior prompt content and metadata (version, hash, card).
   - Revert `main` or `prod` branch if applicable.
   - Update `schemas/prompt-version-schema.yml` to reflect reversion (e.g., `v1.2.1-rollback`).

3. **Re-run Eval Suite**

   - Re-run evals to confirm integrity of restored prompt.
   - Use:
     - `evals/eval-config.promptfoo.yml`
     - `ci/eval-gate.yml`

4. **Log the Rollback**

   - Append an entry to:
     - `audit/artifact-audit-log.md`
     - `schemas/prompt-change-log.yml`
   - Include:
     - Reason for rollback
     - Who authorized it
     - Link to related eval failures or logs

5. **Notify Stakeholders**
   - Internal message, Slack alert, or system notification to relevant teams.
   - Include rollback version and audit link.

---

## Rollback Checklist

| Task                    | File Reference                      |
| ----------------------- | ----------------------------------- |
| Last good version found | `schemas/prompt-version-schema.yml` |
| Eval re-run successful  | `evals/eval-config.promptfoo.yml`   |
| CI passed               | `ci/eval-gate.yml`                  |
| Rollback logged         | `audit/artifact-audit-log.md`       |
| Change log updated      | `schemas/prompt-change-log.yml`     |
| Stakeholders notified   | N/A                                 |

---

## Related Workflows

- Prompt Lifecycle Diagram → `prompt-lifecycle-diagram.md`
- Promotion Pipeline → `promotion-pipeline.md`
- Eval Gating → `ci/eval-gate.yml`

---

## Summary

Rollback is a safety-critical component of any prompt governance system. This flow ensures version traceability, fast recovery, and stakeholder confidence in the face of LLM drift or regression.
