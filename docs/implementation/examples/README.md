# Examples

This folder contains full lifecycle examples that demonstrate how to use the PromptOps governance artifact in practice.

These examples are designed for:

- LLM engineers implementing CI-gated prompt development workflows
- Governance leads evaluating reproducibility, rollback, and eval coverage
- SaaS SDK platform teams interested in artifact reuse and adoption

Each file in this directory walks through real prompt lifecycle flows using the actual schemas, configs, and evaluation scaffolds from this repo.

## 📂 File Index

| File                                                           | Description                                                                        |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [`eval-gating-in-ci.md`](./eval-gating-in-ci.md)               | Full walkthrough of CI evaluation gating using Promptfoo and governance thresholds |
| [`agent-verification-chain.md`](./agent-verification-chain.md) | Example of a multi-step agent chain with embedded self-verification logic          |
| [`rag-pipeline-lifecycle.md`](./rag-pipeline-lifecycle.md)     | End-to-end RAG governance lifecycle from prompt to fallback safety                 |
| [`owasp-llm-checklist.md`](owasp-llm-checklist.md)             | Governance-aligned checklist based on OWASP LLM application risks                  |

## Usage

Use these files as references when:

- Building internal governance pipelines
- Reviewing artifact evaluation behavior
- Demonstrating compliance-readiness for SDK buyers or acquirers

Adapt these examples to your production-grade LLM workflows.
