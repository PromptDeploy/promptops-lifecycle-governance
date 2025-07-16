# `prompts/` — Versioned Prompt Metadata

This directory contains versioned prompt definitions used across the PromptOps lifecycle.  
Each file follows the schema defined in `schemas/prompt-version-schema.yml` and includes:

- Semantic versioning (`x.y.z`)
- Prompt metadata (ID, description, changelog, tags)
- Governance fields (`created_by`, `eval_id`, `promotion_stage`)
- Compatibility with CI evaluation, HITL signoff, and rollback

## Purpose

The `prompts/` folder serves as the **source of truth** for all live and in-review prompt artifacts. It ensures:

- Reproducibility across environments (staging, production)
- Traceability through CI, evaluation, and promotion gates
- Governance-readiness for audits and acquirer diligence

## Schema Reference

All prompt files in this directory must conform to:

- [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml)

## Example Files

- `onboarding-v2.yml` — Improved user onboarding prompt
- `support-agent-v1.yml` — Agent fallback prompt for support use cases

> 📌 NOTE: This folder replaces `schemas/prompt-card.example.yml` as the canonical prompt metadata store.
