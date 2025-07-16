# Compliance Mapping Guide: Link Features to Standards Like OWASP, SOC2, NIST

This document maps core features of the PromptOps Lifecycle Governance artifact to emerging governance standards and buyer expectations. Use this table to demonstrate alignment with:

- OWASP Top 10 for LLMs (2025)
- PromptOps emerging best practices (LangSmith, Langfuse, etc.)
- SOC2-style auditability expectations

---

## Standards Mapping Table

| Standard / Expectation                       | Feature / File                                                                                                                                             | Description                                                                      |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **OWASP GenAI #1: Prompt Injection**         | [`schemas/prompt-card.example.yml`](../schemas/prompt-card.example.yml), [`workflows/policy-as-code-example.yml`](../workflows/policy-as-code-example.yml) | Prompts structured and gated via version schema + policy enforcement hooks       |
| **OWASP GenAI #2: Insecure Output Handling** | [`evals/criteria-reference.md`](../evals/criteria-reference.md), [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json)                           | Output schemas include explicit safety/error fields                              |
| **OWASP GenAI #3: Training Data Poisoning**  | N/A                                                                                                                                                        | Artifact assumes upstream model integrity                                        |
| **OWASP GenAI #4: Model Denial of Service**  | [`logs/cost-metrics-schema.yml`](../logs/cost-metrics-schema.yml), [`evals/cost-checks.yml`](../evals/cost-checks.yml)                                     | Cost visibility + per-agent token usage enforcement                              |
| **OWASP GenAI #5: Data Leakage**             | [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json), [`scripts/prompt-eval-runner.py`](../scripts/prompt-eval-runner.py)                       | Logs structured for redaction; recommend PII filters as pre-execution middleware |
| **PromptOps: Prompt Versioning**             | [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml), [`schemas/prompt-change-log.yml`](../schemas/prompt-change-log.yml)           | Fully versioned prompt artifacts with audit deltas                               |
| **PromptOps: Eval Gating**                   | [`evals/eval-config.promptfoo.yml`](../evals/eval-config.promptfoo.yml), [`ci/eval-gate.yml`](../ci/eval-gate.yml)                                         | Prompts require passing evals before promotion                                   |
| **PromptOps: Rollback Support**              | [`workflows/rollback-flow.md`](../workflows/rollback-flow.md), [`logs/log-sample.output.json`](../logs/log-sample.output.json)                             | Traced runs + rollback guide ensure stable fallbacks                             |
| **SOC2: Auditability**                       | [`audit/artifact-audit-log.md`](../audit/artifact-audit-log.md), [`logs/`](../logs/)                                                                       | Full immutable audit log with structured run output                              |
| **SOC2: Access Control (suggested)**         | N/A                                                                                                                                                        | Recommend RBAC at runtime SDK level; artifact outlines approval workflow logic   |
| **LangSmith-style Tracing**                  | [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json), [`logs/log-sample.output.json`](../logs/log-sample.output.json)                           | JSON logs mimic span-based trace schema                                          |
| **Terraform Analogy: Plan vs Apply**         | [`schemas/prompt-change-log.yml`](../schemas/prompt-change-log.yml), [`ci/eval-gate.yml`](../ci/eval-gate.yml)                                             | Prompts must pass policy and eval before being “applied” to production pipelines |

---

## Summary

This artifact is designed to be extensible and compliant by default. Teams adopting this repo can demonstrate traceability, rollback support, evaluation integrity, and prompt safety checks — aligned with emerging enterprise and security standards.

For a full mapping of risks, see [`audit/failure-modes-catalog.md`](../audit/failure-modes-catalog.md).
