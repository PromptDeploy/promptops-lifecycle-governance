# Documentation Index: PromptOps Artifact

Welcome to the PromptOps governance system. This artifact provides reproducible, CI-enforced, governance-grade scaffolds for managing prompts in production — versioned, evaluated, logged, and rollback-safe.

This documentation is organized by functional role and adoption path:

## Quickstart

For new engineers or platform teams installing PromptOps for the first time.

- [What Is PromptOps? A Practical Introduction to Prompt Lifecycle Governance](getting-started/what-is-promptops.md)
- [Adoption Checklist Audit: Track Governance Implementation Progress](getting-started/adoption-checklist.md)
- [Repo Tour: How This PromptOps Governance System Is Structured](getting-started/repo-tour.md)
- [Run a PromptOps Rollout with the Onboarding Playbook](getting-started/rollout-playbook.md)
- [Use the Org Maturity Ladder: Score Governance Readiness in Your Team](getting-started/org-maturity-ladder.md)
- [Onboarding PromptOps for Infra and Platform Teams](getting-started/infra-onboarding-guide.md)
- [FAQs](getting-started/faqs.md)

## Implementation

For engineers and developers implementing evaluations, writing prompt cards, and enforcing CI gates.

- [Setup Guide: Run Your First Prompt Evaluation Pipeline](implementation/setup-guide.md)
- [Makefile Walkthrough: Automate Eval, CI, Dashboard Sync, and More](implementation/makefile-walkthrough.md)
- [Create Your First Prompt Card: A Step-by-Step Authoring Guide](implementation/create-prompt-card.md)
- [Version and Tag a Prompt: Semantic Control for Safe Deployment](implementation/version-and-tag.md)
- [Writing Prompt Changelogs: Track Edits Across Lifecycle Stages](implementation/writing-changelogs.md)
- [Prompt Lifecycle Walkthrough: From Authoring to Promotion](implementation/promptops-lifecycle-trace.md)
- [Sync Prompt Dashboards for Teams and PMs](implementation/sync-dashboards.md)
- [Prompt Design Patterns: Structures That Survive CI and Promotion](implementation/prompt-design-patterns.md)
- [Governing Multiple Prompts: Scale Versioning, Testing, and Approval Across Teams](implementation/multi-prompt-governance.md)
- [Introduction to Promptfoo Evals: Scoring Prompt Outputs with Confidence](implementation/intro-to-promptfoo.md)
- [Writing Eval Test Cases: Define What Good Looks Like](implementation/writing-eval-test-cases.md)
- [Enforcing CI Eval Gates: Block Unsafe Prompts Before They Ship](implementation/ci-eval-gates.md)
- [Developer Integration Guide](implementation/dev-guide.md)
- [Troubleshooting Guide: Fix Broken Evals, Logs, or CI Workflows](implementation/troubleshooting.md)

## Governance

For AI governance teams, auditors, and platform owners implementing reproducible prompt QA.

- [Prompt Injection Testing: Add Jailbreak Scenarios to Your Eval Suite](governance/prompt-injection-tests.md)
- [RAG Eval Scenarios: Test Context Relevance, Ambiguity, and Fallback Behavior](governance/rag-evals.md)
- [Detect and Mitigate Prompt Drift: Stay Stable Across Model Updates](governance/drift-detection.md)
- [Prompt Logging Guide: Structure Logs for Audit, Debugging, and Cost Analysis](governance/log-field-guide.md)
- [Log Schema Explained: What Each Field Means (and Why It Matters)](governance/log-schema-explained.md)
- [Cost Metrics Dashboard: Visualize Token Spend and Inference ROI](governance/cost-dashboard.md)
- [Policy-as-Code Guide: Enforce Governance Rules with YAML](governance/policy-as-code.md)
- [Approval Processes: Manual vs Automated Prompt Promotion](governance/approval-flows.md)
- [Roll Back a Bad Prompt: Respond to Eval Failures or Production Drift](governance/rollback-guide.md)
- [OWASP LLM Top 10 Deep Dive: How PromptOps Maps to Each Risk](governance/owasp-top10.md)
- [Failure Mode Casebook: Real-World LLM Pitfalls and How to Catch Them](governance/failure-mode-casebook.md)
- [PromptOps Failure Modes in the Wild: What Breaks (and How to Catch It)](governance/promptops-failure-modes.md)
- [Compliance Mapping Guide: Link Features to Standards Like OWASP, SOC2, NIST](governance/compliance-mapping.md)
- [Agent Log Analysis: Trace Reasoning, Tool Use, and Output Cost Step-by-Step](governance/agent-log-analysis.md)
- [Agent Log Analysis (Part II): Track Decisions, Observations, and Token Spend](governance/agent-log-analysis-part-ii.md)
- [Agent Logging Schema](governance/agent-logging.md)
- [Agent Governance](governance/agent-governance.md)
- [Designing Agent Chains: Planner → Verifier → Executor Patterns](governance/agent-patterns.md)
- [Integrate PromptOps with CrewAI or LangGraph](governance/integrate-with-crewai-langgraph.md)

## Licensing & Diligence

For SaaS SDK buyers, platform integrators, or acquirers evaluating PromptOps as a licensing-grade governance artifact.

- [PromptOps Buyer Playbook: What This Repo Offers SDK Buyers and Acquirers](licensing/buyer-playbook.md)
- [Ship a Governed Feature End-to-End: Real PromptOps in Production](licensing/end-to-end-example.md)
- [Govern Your First Agent: From Prompt to Eval to Audit Trail](licensing/govern-first-agent.md)
- [Deploy a Governed RAG Pipeline: Test, Gate, and Monitor Every Step](licensing/governed-rag-pipeline.md)
- [Onboarding Playbook](licensing/onboarding-playbook.md)
- [PromptOps vs AgentOps: Governance for Prompts, Agents, and Everything Between](licensing/promptops-vs-agentops.md)
- [PromptOps QA Checklist: What to Verify Before You Ship](licensing/qa-checklist.md)

## Additional Resources

- `examples/` → Lifecycle walkthroughs (CI, agent chains, RAG pipelines)
- `integration-guides/` → SDK-specific adoption patterns
- `schemas/` → Prompt metadata schemas and dashboards
- `evals/` → Evaluation configs, test cases, cost-check policies
- `logs/` → Prompt and agent output logs with schema enforcement

> For full repo structure, CI usage, Makefile commands, and license terms, see the [Root README](../README.md).
