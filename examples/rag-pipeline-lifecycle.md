# RAG Pipeline PromptOps Lifecycle

This example shows how to apply PromptOps Lifecycle Governance to a typical RAG (Retrieval-Augmented Generation) system.

---

## Scenario

You’re maintaining a production RAG system that uses:

- `LangChain` to compose the pipeline
- `Pinecone` to store embeddings
- A central RAG query prompt that can change over time

---

## Lifecycle Stages Covered

| Stage          | Action                                                                                                                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Versioning** | RAG prompt is tracked in [`schemas/prompt-version-schema.yml`](../../schemas/prompt-version-schema.yml) and changes logged in [`schemas/prompt-change-log.yml`](../../schemas/prompt-change-log.yml) |
| **Evaluation** | Prompt updates must pass evals defined in [`evals/eval-config.promptfoo.yml`](../../evals/eval-config.promptfoo.yml)                                                                                 |
| **Logging**    | Each run is logged to [`logs/prompt-log-schema.json`](../../logs/prompt-log-schema.json) with output, tokens, retrieved docs                                                                         |
| **Promotion**  | Prompt moves from dev → staging → prod via gated steps in [`workflows/promotion-pipeline.md`](../../workflows/promotion-pipeline.md)                                                                 |
| **Rollback**   | Fallbacks are defined in [`workflows/rollback-flow.md`](../../workflows/rollback-flow.md) to handle context drift or hallucinations                                                                  |

---

## Real-World Failures Covered

| Failure                | Mitigation                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Retrieval miss         | Improve embeddings, reframe prompt, add reranker                                   |
| Prompt drift           | Use versioned prompt schemas with audit logs                                       |
| Accuracy drop          | CI evals catch regressions                                                         |
| Cost spike             | [`evals/cost-checks.yml`](../../evals/cost-checks.yml) flags increased token usage |
| Hallucinated citations | Regression tests check against ground truth documents                              |

---

## GitHub Action Flow

RAG prompt edits are tested automatically:

```yaml
# In ci/eval-gate.yml
- name: Run Promptfoo on RAG prompt
  run: python scripts/prompt-eval-runner.py --config evals/eval-config.promptfoo.yml
```

## Bonus: Prompt Example

Here’s a RAG prompt example stored in schemas/prompt-card.example.yml:

```yaml
name: "RAG Query Prompt"
version: "v1.3.0"
tags: ["rag", "retrieval", "fallback"]
description: "Answer questions using the provided context. If unsure, say 'Not enough information.'"
```

---

## Why This Matters

- PromptOps makes RAG pipelines reproducible
- Regression-tested prompts protect QA
- Rollback and change logs reduce risk
- Aligns with PromptOps, OWASP GenAI, and enterprise audit needs

## See Also

- integration-guides/pinecone.md
- evals/criteria-reference.md
- logs/log-sample.output.json
