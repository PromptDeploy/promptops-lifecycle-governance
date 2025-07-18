# What Is PromptOps? A Practical Introduction to Prompt Lifecycle Governance

In production environments, prompt artifacts are subject to the same risks as software code — drift, regression, brittleness, and silent failures. Yet most teams still treat prompt engineering as an ad hoc craft:

- Undocumented edits in shared Notion docs
- Prompts manually copied into frontend code with no changelog
- Production prompts “improved” live without eval checks or rollback

Here are just a few examples:

- A search assistant silently stopped returning results after a junior engineer tweaked the prompt to “sound friendlier,” causing logic clauses to break — no evals, no diff, no logs.
- An enterprise chatbot began hallucinating pricing info after a prompt was edited post-launch to improve tone — but no one re-ran regression evals or reviewed the change via HITL.
- A support agent system degraded over weeks due to prompt drift from multiple contributors — with no prompt versioning, no rollback pipeline, and no logging. Debugging took days.

## Why PromptOps Exists

**PromptOps** introduces a structured, reproducible governance layer around prompts — analogous to what DevOps and MLOps provide for code and models. It answers key operational questions:

- Who changed this prompt, and why?
- Has it passed evaluation thresholds?
- Can we revert it safely?
- Are we logging how it behaves in production?
- Has it gone through human-in-the-loop review?

Without PromptOps, teams risk production regressions with zero visibility — and governance teams face audit blind spots that undermine buyer trust and operational safety.

## What PromptOps Governs (The Core Lifecycle)

PromptOps formalizes the prompt development lifecycle into six reproducible phases:

### 1. **Prompt Creation + Versioning**

Prompts are authored and committed using the [**PromptCard™ Schema**](../../schemas/prompt-version-schema.yml) with semantic versioning and metadata.

```yaml
id: onboarding-v2
description: Improved user onboarding assistant prompt
version: 2.1.0
tags:
  - onboarding
  - assistant
created_by: dev-a
changelog: |
  - Tuned tone for friendliness
  - Improved coverage for edge-case intents
```

### 2. **Evaluation + CI Gating**

Each prompt must pass CI evaluation thresholds using the [**PromptEval™ CI Gate**](../../ci/eval-gate.yml) and the configurable [**EvalSuite™ Core Config**](../../evals/evalsuite-core-config.yml).

```yaml
name: Eval-Gate
on:
  pull_request:
    paths:
      - "prompts/**"
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - name: Run evals
        run: promptfoo eval -c evals/evalsuite-core-config.yml
```

### 3. **Human-in-the-Loop (HITL) Improvement**

The [**HITLSignoff™ Template**](../../workflows/HITL_Approval_Template.md) ensures that prompts are reviewed and approved before going live.

### 4. **Promotion + Deployment**

Approved prompts are staged using the [**PromptPromote™ Protocol**](../../workflows/promotion-pipeline.md), which supports environment tagging and checksum pinning.

### 5. **Logging + Traceability**

All prompt executions are logged via [**PromptLog™ Schema**](../../schemas/prompt-log-schema.json) and [**AgentTrace™ Log Schema**](../../schemas/agenttrace-schema.json) to ensure full traceability across versions, costs, and results.

### 6. **Rollback**

Failures or regressions trigger the [**SafeRevert™ Rollback Flow**](../../workflows/rollback-flow.md), which reverts to a previous prompt version after revalidation.

---

## Where PromptOps Lives in This Repo

| Component Name                                                       | Description                                      |
| -------------------------------------------------------------------- | ------------------------------------------------ |
| [PromptCard™ Schema](../../schemas/prompt-version-schema.yml)        | Defines structure for versioned prompts          |
| [PromptVersion™ Metadata](../../schemas/prompt-change-log.yml)       | Semantic versioning, changelog, tag logic        |
| [EvalSuite™ Config](../../evals/evalsuite-core-config.yml)           | Evaluation configs for prompt behavior checks    |
| [PromptEval™ CI Gate](../../ci/eval-gate.yml)                        | CI logic for enforcing eval thresholds           |
| [HITLSignoff™ Template](../../workflows/HITL_Approval_Template.md)   | Checklist for manual approval                    |
| [PromptPromote™ Protocol](../../workflows/promotion-pipeline.md)     | Safe rollout and version pinning process         |
| [PromptLog™ Schema](../../schemas/agenttrace-schema.json)            | JSON log format for prompt execution             |
| [AgentTrace™ Output Schema](../../schemas/agenttrace-schema.json)    | Logs agent reasoning, cost, and token flow       |
| [SafeRevert™ Rollback Flow](../../workflows/rollback-flow.md)        | Rollback strategy for failed prompt deployments  |
| [PromptFail™ Risk Catalog](../governance/promptops-failure-modes.md) | Known failure patterns and prevention strategies |

---

## Learn More

→ [From Version to Rollback: A Real PromptOps Lifecycle in Action](../docs/implementation/promptops-lifecycle-trace.md)
