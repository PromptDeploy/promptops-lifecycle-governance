# Agent Verification Chain (Multi-Agent Governance Pattern)

This example demonstrates how to apply PromptOps governance to a multi-agent LLM system.

It focuses on **verifier-planner-actor** agent flows, a common architecture in LangGraph, OpenAgents, and other orchestration tools.

---

## Scenario

A multi-agent chain for document processing:

1. **Planner Agent**: Decides on actions
2. **Actor Agent**: Executes actions
3. **Verifier Agent**: Checks correctness

The chain is fragile when:

- Prompts drift independently
- Agents disagree on task scope
- Failures aren’t logged or rolled back

---

## PromptOps Governance Layers

| Layer             | File(s) Used                                                                                                                                           | What It Does                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Versioning**    | [`schemas/prompt-version-schema.yml`](../../schemas/prompt-version-schema.yml), [`schemas/prompt-change-log.yml`](../../schemas/prompt-change-log.yml) | Ensures all agents use coordinated prompt versions         |
| **Evaluation**    | [`evals/test-cases.json`](../../evals/test-cases.json), [`ci/eval-gate.yml`](../../ci/eval-gate.yml)                                                   | CI ensures verifier-agent accuracy doesn't drop            |
| **Logging**       | [`schemas/prompt-log-schema.json`](../../schemas/prompt-log-schema.json), [`logs/log-sample.output.json`](../../logs/log-sample.output.json)           | Tracks which agent ran what and with what result           |
| **Rollback**      | [`workflows/rollback-flow.md`](../../workflows/rollback-flow.md)                                                                                       | Fallbacks defined if verifier disagrees or planner fails   |
| **Orchestration** | [`workflows/agent-orchestration-guide.md`](../../workflows/agent-orchestration-guide.md)                                                               | Describes agent roles and prompt compatibility assumptions |

---

## Governance Flow

1. Planner prompt is versioned → `schemas/`
2. Change is logged → `prompt-change-log.yml`
3. CI tests verifier accuracy → `evals/`
4. If passing, prompt is promoted → `promotion-pipeline.md`
5. All agent runs are logged → `logs/`
6. If verifier fails, rollback to last stable planner → `rollback-flow.md`

---

## Prompt Design Example

```yaml
name: "Verifier Agent Prompt"
version: "v1.1.0"
description: "Given a task plan and action result, verify alignment with system rules."
tags: ["agent", "verifier", "chain-of-thought"]
```

---

## Why This Matters

Without governance:

- Verifier may reject valid actor behavior due to stale logic
- Planner may hallucinate unsupported actions
- Debugging agent failures is painful without logs or traceability

With PromptOps:

- Agents align on shared prompt contracts
- Logs reveal what went wrong and why
- Teams can update verifier logic without breaking production

## See Also

- workflows/agent-orchestration-guide.md
- examples/rag-pipeline-lifecycle.md
- audit/failure-modes-catalog.md
