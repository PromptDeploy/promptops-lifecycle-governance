# PromptOps Developer Guide

This guide is for engineers integrating PromptOps governance into their LLM pipelines.

## 📂 Folder Structure Overview

| Folder                | Purpose                                                               |
| --------------------- | --------------------------------------------------------------------- |
| `schemas/`            | Prompt version metadata, dashboard views, and version tags            |
| `evals/`              | Promptfoo eval configs + test cases (base, variants, RAG, comparison) |
| `logs/`               | Cost + trace logs, JSON schema for structured auditability            |
| `ci/`                 | CI gating configs (pass/fail logic, prod enforcement)                 |
| `workflows/`          | HITL approval templates, rollback flows, promotion logic              |
| `examples/`           | OWASP checklists, agent behaviors, prompt summaries                   |
| `integration-guides/` | LangChain, OpenAPI, Pinecone usage tips                               |
| `scripts/`            | CLI utilities for running evals or generating prompt views            |
| `tests/`              | Regression tests for different prompt scenarios                       |
| `audit/`              | Logs, HITL checklists, failure mode references                        |

---

## Common Engineer Tasks

### Run all governance tests (CI gate)

```bash
make test
```

### Run in preview mode (non-blocking)

```bash
make eval
```

### Re-run eval against previous output only

```bash
make strict-eval
```

---

### Run Prompt Injection Tests

```bash
promptfoo test --config evals/eval-config.promptfoo.yml --tests evals/prompt-injection-tests.json
```

---

### Run RAG fallback evals

```bash
promptfoo test --config evals/eval-config.rag.promptfoo.yml
```

---

## Prompt Metadata & Versions

- Edit the canonical prompt here:

  ```
  schemas/prompt-card.example.yml
  ```

- Sync dashboard view (for PMs):

  ```bash
  python scripts/generate-dashboard-card.py
  ```

- Approved version for production lives in:
  ```
  schemas/prompt-version.prod-approved.yml
  ```

---

## Eval Configs at a Glance

| Purpose                | Config File                               |
| ---------------------- | ----------------------------------------- |
| Standard CI Eval       | `evals/eval-config.promptfoo.yml`         |
| Fuzzed Prompt Variants | `evals/eval-config.variant.promptfoo.yml` |
| RAG fallback behavior  | `evals/eval-config.rag.promptfoo.yml`     |
| Claude vs GPT compare  | `evals/eval-config.compare.promptfoo.yml` |

Test cases live in:

```
evals/test-cases*.json
```

---

## Governance Triggers

Thresholds enforced via:

- `ci/ci-prod-block.yml`
- Score ≥ 0.85, Pass rate ≥ 90%
- Rollback if cost spike > 20% or hallucinations detected

HITL approval template:

```
workflows/HITL_Approval_Template.md
```

---

## Logs and Observability

- All logs conform to:

  ```
  logs/prompt-log-schema.json
  ```

- Sample outputs:

  ```
  logs/log-sample.output.json
  ```

- Supports OpenTelemetry-style traceability

---

## Dev Hygiene (Optional)

Consider adding:

- `make format` for YAML/JSON formatting
- `make lint` for prompt schema validation

---

Need help? Check:

- [docs/agent-governance.md](agent-governance.md)
- [docs/faqs.md](faqs.md)
