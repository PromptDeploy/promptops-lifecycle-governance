# Documentation Index: PromptOps Artifact

Welcome to the PromptOps governance system. This artifact provides reproducible, CI-enforced, governance-grade scaffolds for managing prompts in production — versioned, evaluated, logged, and rollback-safe.

This documentation is organized by functional role and adoption path:

## Getting Started

For new readers, platform teams exploring PromptOps, or anyone evaluating its purpose and architecture.

- [What Is PromptOps?](getting-started/what-is-promptops.md)
- [FAQs](getting-started/faqs.md)

## Implementation

For engineers and developers installing PromptOps workflows, running evaluations, and modifying CI pipelines.

- [Prompt Lifecycle Trace](implementation/promptops-lifecycle-trace.md)
- [Developer Integration Guide](implementation/dev-guide.md)

## Governance

For AI governance teams, policy owners, and risk auditors validating governance pillar coverage and operational readiness.

- [Agent Governance](governance/agent-governance.md)
- [Agent Logging Schema](governance/agent-logging.md)
- [Org Maturity Ladder](governance/org-maturity-ladder.md)

## Licensing & Diligence

For SaaS SDK buyers, platform integrators, and acquirers evaluating PromptOps as a licensing-grade governance artifact.

- [Onboarding Playbook](licensing/onboarding-playbook.md)
- [Adoption Checklist](licensing/adoption-checklist.md)

> `licensing-package-map.md` and `diligence-readiness-checklist.md` will be included in the next vault update.

## Additional Resources

- `examples/` → Lifecycle walkthroughs (CI, agent chains, RAG pipelines)
- `integration-guides/` → SDK-specific adoption patterns
- `schemas/` → Prompt metadata schemas and dashboards
- `evals/` → Evaluation configs, test cases, cost-check policies
- `logs/` → Prompt and agent output logs with schema enforcement
