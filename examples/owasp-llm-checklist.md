# OWASP LLM Security Checklist Mapping

This file shows how the PromptOps Lifecycle Governance artifact aligns with the OWASP Top 10 for Large Language Models (2025).

Each item is mapped to a corresponding file or governance pattern in this repo.

---

## OWASP LLM Top 10 Compliance

| OWASP Issue                            | Covered By                                                                                                                                                       | Description                                                         |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **1. Prompt Injection**                | [`schemas/prompt-card.example.yml`](../../schemas/prompt-card.example.yml), [`workflows/policy-as-code-example.yml`](../../workflows/policy-as-code-example.yml) | Prompts are schema-bound and enforced with policy hooks             |
| **2. Insecure Output Handling**        | [`evals/test-cases.json`](../../evals/test-cases.json), [`logs/prompt-log-schema.json`](../../logs/prompt-log-schema.json)                                       | Tests cover hallucinations, errors are logged clearly               |
| **3. Training Data Poisoning**         | (Out of scope — upstream model assumption)                                                                                                                       | Artifact assumes model integrity; mitigated at model provider level |
| **4. Model Denial of Service**         | [`evals/cost-checks.yml`](../../evals/cost-checks.yml), [`logs/cost-metrics-schema.yml`](../../logs/cost-metrics-schema.yml)                                     | Cost evaluation and token tracking in CI                            |
| **5. Data Leakage**                    | [`logs/prompt-log-schema.json`](../../logs/prompt-log-schema.json), [`scripts/prompt-eval-runner.py`](../../scripts/prompt-eval-runner.py)                       | Logs support PII filters and runtime input/output control           |
| **6. Unauthorized Code Execution**     | [`workflows/policy-as-code-example.yml`](../../workflows/policy-as-code-example.yml)                                                                             | Policies can block code execution based on prompt pattern           |
| **7. Model Theft / Leakage**           | (Partially covered)                                                                                                                                              | Prompt versioning supports integrity, not full DRM                  |
| **8. Supply Chain Vulnerabilities**    | [`ci/log-schema-check.yml`](../../ci/log-schema-check.yml), [`Makefile`](../../Makefile)                                                                         | Validations and lockfile-aware install for minimal drift            |
| **9. Inadequate Monitoring / Logging** | [`logs/`](../../logs/), [`scripts/prompt-eval-runner.py`](../../scripts/prompt-eval-runner.py)                                                                   | Full lifecycle logging, eval failures, cost metrics                 |
| **10. Misaligned Objective Function**  | [`evals/eval-config.promptfoo.yml`](../../evals/eval-config.promptfoo.yml)                                                                                       | Evaluation criteria explicitly defined and enforced in CI           |

---

## Summary

This artifact allows teams to:

- Map their prompt workflows to OWASP GenAI risks
- Add CI gates to reduce production failure risk
- Maintain audit logs and fallback plans for regulated environments

Use this checklist to justify governance investments to security and compliance teams.

---

> Last updated: 2025-07-14
