# PromptOps Lifecycle Governance — Repo Manifest

This repository provides a fully installable PromptOps governance scaffold for teams. It includes schemas, eval configs, policy workflows, audit logs, and integration guides that enable prompt versioning, evaluation gating, agent orchestration, and governance-grade reproducibility.

## 🏗️ Build Metadata

| Field              | Value                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| Artifact ID        | `ART-20250710-001`                                                                              |
| Build Date         | `2025-07-10`                                                                                    |
| Governance Pillars | PromptOps, Evaluation, Logging, Cost/ROI, Agent Governance, Promotion/Rollback, Audit Readiness |
| Repo Version Hash  | `d8c3b1f` _(use latest commit or tag)_                                                          |
| Vault Packaging    | `v0.2.0`                                                                                        |
| Licensing Status   | ✅ MIT (internal use) · 🔒 Commercial use requires license                                      |

## Directory & File Overview

| Path                 | Description                                                                              | Related Usage Guide |
| -------------------- | ---------------------------------------------------------------------------------------- | ------------------- |
| `README.md`          | Audience-indexed documentation for governance, implementation, licensing, and onboarding | –                   |
| `LICENSE.txt`        | Repository license for distribution and reuse                                            | –                   |
| `Makefile`           | CLI commands for setup, evals, and test automation                                       | –                   |
| `requirements.txt`   | Python dependencies for scripts and evaluation tools                                     | –                   |
| `CHANGELOG.md`       | Version history of the artifact                                                          | –                   |
| `REPO_MANIFEST.md`   | This file: inventory of repo deliverables                                                | –                   |
| `LICENSE_PACKAGE.md` | Licensing terms for reuse, OEM, and integration                                          | –                   |

## Evaluation System (`/evals`)

| File                        | Description                                               | Related Guide                                                |
| --------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| `evalsuite-core-config.yml` | Promptfoo configuration file for running evaluations      | [`eval-gating-in-ci.md`](../examples/eval-gating-in-ci.md)   |
| `test-cases.json`           | Dataset of prompt-input/output test cases                 | [`criteria-reference.md`](criteria-reference.md)             |
| `cost-checks.yml`           | YAML rule definitions for token usage and cost thresholds | [`cost-metrics-schema.yml`](../logs/cost-metrics-schema.yml) |
| `criteria-reference.md`     | Definitions of pass/fail criteria and scoring strategies  | [`eval-gating-in-ci.md`](../examples/eval-gating-in-ci.md)   |

## Observability & Logs (`/logs`)

| File                      | Description                                          | Related Guide                                              |
| ------------------------- | ---------------------------------------------------- | ---------------------------------------------------------- |
| `prompt-log-schema.json`  | Canonical schema for logging prompt inputs/outputs   | [`log-field-guide.md`](log-field-guide.md)                 |
| `log-sample.output.json`  | Example log output for observability tooling         | [`log-field-guide.md`](log-field-guide.md)                 |
| `cost-metrics-schema.yml` | Cost telemetry format with fields for token tracking | [`eval-gating-in-ci.md`](../examples/eval-gating-in-ci.md) |
| `log-field-guide.md`      | Field-by-field explanation of log schemas            | –                                                          |

## Prompt Schemas (`/schemas`)

| File                        | Description                                             | Related Guide                                                             |
| --------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| `prompt-card.example.yml`   | Full metadata example of a versioned prompt card        | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |
| `prompt-change-log.yml`     | Format for tracking prompt edits across environments    | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |
| `prompt-version-schema.yml` | Core schema defining prompt metadata and lifecycle tags | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |

## CI/CD Workflows (`/ci` & `/workflows`)

| File                                     | Description                                                  | Related Guide                                                             |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| `ci/eval-gate.yml`                       | GitHub Action: blocks PRs until evals pass                   | [`ci-eval-gate.yml`](../examples/ci-eval-gate.yml)                        |
| `ci/log-schema-check.yml`                | CI test to validate log schema integrity                     | [`log-field-guide.md`](../logs/log-field-guide.md)                        |
| `workflows/promotion-pipeline.md`        | Manual or automated flow for promoting prompts across stages | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |
| `workflows/rollback-flow.md`             | Fallback procedure for failed prompt versions                | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |
| `workflows/prompt-lifecycle-diagram.md`  | Diagram showing prompt flow from dev → prod                  | –                                                                         |
| `workflows/policy-as-code-example.yml`   | Declarative rules for prompt governance                      | [`prompt-lifecycle-diagram.md`](../workflows/prompt-lifecycle-diagram.md) |
| `workflows/agent-orchestration-guide.md` | Governance patterns for multi-agent routing and role control | [`agent-verification-chain.md`](../examples/agent-verification-chain.md)  |

## Audit & Risk Mapping (`/audit`)

| File                       | Description                                             | Related Guide                                                  |
| -------------------------- | ------------------------------------------------------- | -------------------------------------------------------------- |
| `artifact-audit-log.md`    | Audit trail template for prompt changes and model usage | [`owasp-llm-checklist.md`](../examples/owasp-llm-checklist.md) |
| `compliance-mapping.md`    | Mapping of artifact features to OWASP, SOC2, etc.       | [`owasp-llm-checklist.md`](../examples/owasp-llm-checklist.md) |
| `failure-modes-catalog.md` | Catalog of common LLM failure patterns & mitigations    | [`owasp-llm-checklist.md`](../examples/owasp-llm-checklist.md) |

## Tests & Scripts

| File                                | Description                                     | Related Guide                                              |
| ----------------------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `tests/prompt-regression.test.json` | Golden tests to detect prompt regressions       | [`eval-gating-in-ci.md`](../examples/eval-gating-in-ci.md) |
| `scripts/prompt-eval-runner.py`     | Script to trigger prompt evals locally or in CI | [`eval-gating-in-ci.md`](../examples/eval-gating-in-ci.md) |

---

## Examples & Use Cases (`/examples`)

| File                          | Description                                        | Related Guide                                                               |
| ----------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| `eval-gating-in-ci.md`        | Guide for enforcing evals as a CI gating mechanism | [`ci-eval-gate.yml`](../examples/ci-eval-gate.yml)                          |
| `agent-verification-chain.md` | Agent self-checking and verification patterns      | [`agent-orchestration-guide.md`](../workflows/agent-orchestration-guide.md) |
| `owasp-llm-checklist.md`      | Applied security checklist using OWASP Top 10      | [`failure-modes-catalog.md`](../audit/failure-modes-catalog.md)             |
| `rag-pipeline-lifecycle.md`   | Full lifecycle governance of a RAG pipeline        | [`pinecone.md`](../integration-guides/pinecone.md)                          |

## Integration Guides (`/integration-guides`)

| File                    | Description                                          | Related Guide                                                            |
| ----------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| `langchain.md`          | Governance scaffolds for LangChain pipelines         | [`langchain-snippets.py`](langchain-snippets.py)                         |
| `pinecone.md`           | Prompt governance within Pinecone/RAG workflows      | [`rag-pipeline-lifecycle.md`](../examples/rag-pipeline-lifecycle.md)     |
| `openapi-agent.md`      | Handling safety and logging for OpenAPI-based agents | [`agent-verification-chain.md`](../examples/agent-verification-chain.md) |
| `langchain-snippets.py` | Annotated snippets for prompt tracing in LangChain   | [`langchain.md`](langchain.md)                                           |

## Documentation (`/docs`)

| File or Folder          | Description                                    | Primary Audience              |
| ----------------------- | ---------------------------------------------- | ----------------------------- |
| `docs/index.md`         | Central doc index linking all guidance         | All users                     |
| `docs/getting-started/` | Overview, what-is, FAQs                        | First-time readers, engineers |
| `docs/implementation/`  | CI integration, dev guide                      | Infra teams, prompt engineers |
| `docs/governance/`      | Governance maturity, logging, agent control    | AI policy teams               |
| `docs/licensing/`       | Onboarding, diligence checklist, packaging map | Buyers, acquirers             |
