# Evaluation Configs

This folder contains all evaluation artifacts used to test and govern prompt behavior across CI, development, and production scenarios.

Evaluations are run automatically in CI (see `ci/eval-gate.yml`) and can also be used manually for local prompt testing.

## Purpose

The goal of PromptOps evaluation is to enforce:

- Prompt correctness and stability across versions
- Safety and hallucination thresholds
- Cost governance (token/price ceilings)
- Regressions and edge-case resilience

## File Index

| File                                                                       | Description                                        |
| -------------------------------------------------------------------------- | -------------------------------------------------- |
| [`evalsuite-core-config.yml`](./evalsuite-core-config.yml)                 | Main Promptfoo config for CI test runs             |
| [`test-cases.json`](./test-cases.json)                                     | Core test suite used in CI and manual runs         |
| [`test-cases.variant.json`](./test-cases.variant.json)                     | Optional variant prompt regression cases           |
| [`cost-checks.yml`](./cost-checks.yml)                                     | Policy check for token/inference cost ceilings     |
| [`eval-config.rag.promptfoo.yml`](./eval-config.rag.promptfoo.yml)         | RAG-specific eval configuration                    |
| [`eval-config.variant.promptfoo.yml`](./eval-config.variant.promptfoo.yml) | Alternative eval logic for variant runners         |
| [`eval-report.rag.md`](./eval-report.rag.md)                               | Example eval run report (for logging or QA review) |
| [`prompt-injection-tests.json`](./prompt-injection-tests.json)             | Injection attempts for safety regressions          |

## How to Run

To run CI-aligned evaluations locally:

```bash
promptfoo evaluate -c evals/evalsuite-core-config.yml
```

Or with `make` (if defined):

```bash
make eval
```

Results can be saved and processed using:

```bash
--output json --output-file evals/.local-results.json
```

## Governance Integration

Evaluations are required for:

- CI merge gating ([`ci/eval-gate.yml`](../ci/eval-gate.yml))
- Prompt promotion ([`workflows/promotion-pipeline.md`](../workflows/promotion-pipeline.md))
- Rollback validation ([`workflows/rollback-flow.md`](../workflows/rollback-flow.md))
- HITL signoff prep ([`workflows/HITL_Approval_Template.md`](../workflows/HITL_Approval_Template.md))

## Licensing Note

These test cases and configs are part of the reproducibility layer for prompt governance. When licensing PromptOps artifacts, include `evals/` as part of the proof-of-use package.
