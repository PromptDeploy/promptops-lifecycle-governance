# Prompt Lifecycle Walkthrough: From Authoring to Promotion

This tutorial traces a real prompt through its full governance lifecycle using this repo’s scaffolds — from versioning and evaluation to HITL signoff, promotion, logging, and rollback.

It assumes the reader is familiar with [What Is PromptOps?](../getting-started/what-is-promptops.md).

## Step 1: Author and Version the Prompt

Create a new prompt definition under `prompts/`. Follow `schemas/prompt-card.example.yml`.

```yaml
id: support-agent-v2
description: Improve error-handling instructions for edge-case queries
version: 2.0.0
tags:
  - support
  - agent
created_by: dev-b
changelog: |
  - Added clarifying fallback message
  - More explicit handling of “not a bug” cases
```

Schema enforced by: [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml)

## Step 2: Add Eval Config and Test Cases

Edit or duplicate from:

- [`evals/evalsuite-core-config.yml`](../evals/evalsuite-core-config.yml)
- [`evals/test-cases.json`](../evals/test-cases.json)

Include cases for success/failure and edge-case behavior.

```json
[
  {
    "input": "It’s not working.",
    "expected_class": "escalate_to_agent"
  },
  {
    "input": "I changed nothing but now it broke.",
    "expected_class": "explain_expected_behavior"
  }
]
```

## Step 3: Run Evaluations Locally

```bash
make eval
# or
promptfoo eval -c evals/evalsuite-core-config.yml
```

Log results locally or into:

- [`logs/eval-report.rag.md`](../evals/eval-report.rag.md)
- [`schemas/prompt-log-schema.json`](../schemas/prompt-log-schema.json)

Gate enforced in CI via: [`ci/eval-gate.yml`](../ci/eval-gate.yml)

## Step 4: Submit HITL Signoff

Use:

- [`workflows/HITL_Approval_Template.md`](../workflows/HITL_Approval_Template.md)

```md
## HITL Approval – support-agent-v2

- Reviewer: governance-lead
- Eval Pass Rate: 100% (5/5)
- Risk Comments: Acceptable for prod, edge cases addressed.
- Recommendation: Promote to staging.
```

## Step 5: Promote the Prompt

Trigger promotion by tagging the version or merging to a tracked branch:

- Update: [`workflows/promotion-pipeline.md`](../workflows/promotion-pipeline.md)
- Add checksum trace or promotion ID if required

```yaml
promotion:
  prompt_id: support-agent-v2
  promoted_version: 2.0.0
  env: production
  hash: abc1234
  promoted_by: infra-engineer
```

## Step 6: Log Production Behavior

Confirm structured logs match schema:

- [`schemas/prompt-log-schema.json`](../schemas/prompt-log-schema.json)

Optional: Add logs from `logs/log-sample.output.json` to real `agent-log.example.json`.

```json
{
  "prompt_id": "support-agent-v2",
  "version": "2.0.0",
  "timestamp": "2025-07-15T13:40:00Z",
  "input": "Still broken.",
  "output_class": "explain_expected_behavior",
  "latency_ms": 213,
  "token_cost": 0.007
}
```

## Step 7: Rollback (If Required)

Trigger rollback via:

- [`workflows/rollback-flow.md`](../workflows/rollback-flow.md)

Restore last known good version (e.g. `1.7.2`) after confirming eval safety.

```yaml
rollback:
  prompt_id: support-agent-v2
  target_version: 1.7.2
  reason: Escalation detection failure in prod
  triggered_by: dev-b
  reviewed_by: governance-lead
```

Re-run `promptfoo eval` on rollback version before re-promotion.

## Recap: The PromptOps Lifecycle in Action

| Phase      | Artifact / Action                                       |
| ---------- | ------------------------------------------------------- |
| Versioning | `prompt-card.yml`, `prompt-version-schema.yml`          |
| Evaluation | `evalsuite-core-config.yml`, `test-cases.json`, CI gate |
| HITL       | `HITL_Approval_Template.md`                             |
| Promotion  | `promotion-pipeline.md`, env tags, hashes               |
| Logging    | `prompt-log-schema.json`, sample outputs                |
| Rollback   | `rollback-flow.md`                                      |

## Next Steps

- Add a real test prompt to `prompts/` and run this flow.
- Customize `make` targets for eval + promotion.
- Integrate logs with your agent orchestration trace.
