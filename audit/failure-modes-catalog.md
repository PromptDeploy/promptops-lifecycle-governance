# Failure Modes Catalog

This catalog outlines known failure modes in SaaS LLM systems and how this artifact mitigates them. Mapped to real-world SDK pain points and governance gaps.

> This catalog is part of the PromptOps Lifecycle Governance artifact.
> It is designed to be auditable, reusable, and installable as a compliance module inside SaaS SDK pipelines.

---

## Failure Mode Matrix

| Failure Mode                    | Description                                                   | Real-World Signal / Consequence                                     | Mitigation                                           | Linked Files                                                                                                                                                             |
| ------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Prompt Drift**                | Output behavior changes over time or with model updates       | Model upgrades silently alter behavior; trust breaks; hard to debug | Semantic versioning, change logs, eval gating        | [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml), [`schemas/prompt-change-log.yml`](../schemas/prompt-change-log.yml), [`evals/`](../evals/)  |
| **Prompt Injection**            | User manipulates prompt/system behavior                       | Jailbreaks, unsafe completions                                      | Input constraints, policy enforcement                | [`workflows/policy-as-code-example.yml`](../workflows/policy-as-code-example.yml), [`examples/owasp-llm-checklist.md`](../examples/owasp-llm-checklist.md)               |
| **Undocumented Prompt Changes** | Silent or untracked updates to prompts                        | SOC2 violations, debugging paralysis                                | Prompt metadata, audit logs                          | [`schemas/prompt-card.example.yml`](../schemas/prompt-card.example.yml), [`audit/artifact-audit-log.md`](../audit/artifact-audit-log.md)                                 |
| **Eval Regression**             | Prompt changes introduce undetected quality drop              | Hallucinations, compliance issues                                   | Eval harnesses, CI gates                             | [`evals/eval-config.promptfoo.yml`](../evals/eval-config.promptfoo.yml), [`ci/eval-gate.yml`](../ci/eval-gate.yml)                                                       |
| **Eval Drift**                  | Evaluation behavior changes due to model version shifts       | Missed regressions                                                  | Lock model versions, version eval configs            | [`evals/`](../evals/)                                                                                                                                                    |
| **Multi-Agent Failure**         | Agents misalign, loop, or fail to coordinate                  | LangGraph verifier rejected valid outputs; cascading agent errors   | Orchestration guides, rollback flow, shared memory   | [`workflows/agent-orchestration-guide.md`](../workflows/agent-orchestration-guide.md), [`examples/agent-verification-chain.md`](../examples/agent-verification-chain.md) |
| **Redundant Agent Execution**   | Agents duplicate tasks or overwrite each other                | Cost spikes, wasted tokens                                          | Step logging, output coordination                    | [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json)                                                                                                          |
| **RAG Retrieval Miss**          | Relevant docs not returned                                    | Support bots hallucinate despite having correct KB                  | Embed debugging, improved query phrasing, re-ranking | [`integration-guides/pinecone.md`](../integration-guides/pinecone.md), [`examples/rag-pipeline-lifecycle.md`](../examples/rag-pipeline-lifecycle.md)                     |
| **RAG Context Truncation**      | Retrieved context too large to fit into prompt window         | Model “forgets” key info; incomplete answers                        | Context prioritization logic                         | [`examples/rag-pipeline-lifecycle.md`](../examples/rag-pipeline-lifecycle.md)                                                                                            |
| **Hallucinated Citations**      | Model invents references not in retrieved docs                | Misinformation, user confusion                                      | Ground truth comparison tests                        | [`evals/test-cases.json`](../evals/test-cases.json), [`evals/criteria-reference.md`](../evals/criteria-reference.md)                                                     |
| **Cost Spikes**                 | Token usage explodes due to verbose prompts or infinite loops | Budget overruns, forced shutdowns                                   | Cost evals, token guards, usage logging              | [`evals/cost-checks.yml`](../evals/cost-checks.yml), [`logs/cost-metrics-schema.yml`](../logs/cost-metrics-schema.yml)                                                   |
| **Insecure Output Handling**    | Model outputs unsafe strings (e.g. code, SQL, PII)            | Compliance risks, security vulnerabilities                          | Output schemas, moderation hooks                     | [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json), [`evals/criteria-reference.md`](../evals/criteria-reference.md)                                         |

---

## Summary

This artifact is designed to make LLM-powered systems more observable, testable, and governable. By mapping failure modes to real-world SDK friction points and providing structured mitigations, teams can adopt the repo as a drop-in PromptOps layer aligned with OWASP, SOC2, and emerging PromptOps standards.

> Last updated: 2025-07-14 by Hou Chia
