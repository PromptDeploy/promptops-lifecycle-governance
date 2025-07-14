# Contributing to PromptOps Lifecycle Governance

Thanks for your interest in contributing to this project! This artifact is part of a broader AI-Native Governance Vault designed to help teams version, test, and govern prompt pipelines in production.

## AI-Native Contribution Terms

All contributions must meet human-reviewed engineering standards.

By submitting a pull request, you agree that:

- You are the original author of the contribution, or
- You have full rights to contribute the material under the MIT License.

All AI-generated content must be reviewed, validated, and documented clearly. Please annotate any AI-generated code or artifacts accordingly in your PR descriptions.

## How to Contribute

We welcome:

- Bug fixes and improvements to existing files
- New test cases, evaluation config extensions, or log schema variants
- Clarifications, usage examples, or additional guides
- Governance patterns and safety policy modules

Before contributing:

1. Fork the repository
2. Create a feature branch
3. Write clear, documented commits
4. Submit a pull request with context and reasoning

👉 Need orientation? Start with [`docs/dev-guide.md`](docs/dev-guide.md)

## ✅ What a Good PR Looks Like

To help reviewers understand your changes, include:

1. **Purpose** — What problem does this change solve?
2. **Prompt Impact** — Are you modifying an existing prompt? If yes:
   - Update `prompt-card.example.yml` with a new version and hash
   - Add a `prompt-change-log.yml` entry
3. **Test Coverage** — Add or update entries in:
   - `evals/test-cases.json` or `prompt-injection-tests.json`
4. **CI Compliance** — Confirm `make eval` and `make test` pass
5. **Approval Required?** — For production prompt updates, submit a HITL approval in `/reviews/`

### ✅ Example PR: Prompt Update

feat(prompt): update support-agent prompt for better cost control

- Added fallback handling to avoid context explosion
- Reduced output verbosity to lower avg tokens
- New version: v1.2.1
- Added test case: cost regression check
- HITL approval: ✅ included

## 📦 Usage & Commercial Terms

You are free to use, modify, and integrate this repository into your systems under the terms of the [MIT License](./LICENSE.txt).

Commercial use is permitted with attribution. For OEM, enterprise support, or derivative licensing inquiries, contact the author directly.

## Governance Alignment

This artifact is part of a broader IP Vault focused on:

- Prompt versioning and rollback safety
- Evaluation pipelines for prompt drift and hallucination
- Multi-agent coordination safety
- Observability, cost control, and compliance alignment

Contributions should align with these goals whenever possible.

---

Thank you for helping strengthen the AI-native development ecosystem.
