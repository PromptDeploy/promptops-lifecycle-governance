# Contributing to PromptOps Lifecycle Governance

Thanks for your interest in contributing to this project. This artifact is part of a broader AI-Native Governance Vault designed to help teams version, test, and govern prompt pipelines in production environments.

## Contribution Standards

All contributions must meet human-reviewed engineering standards.

By submitting a pull request, you agree that:

- You are the original author of the contribution, or
- You have full rights to contribute the material under the MIT License.

If your contribution includes any AI-generated code or content, it must be validated, clearly documented, and annotated as such in your PR description.

## What You Can Contribute

We welcome contributions across several domains:

- Bug fixes or improvements to existing files
- New prompt test cases, evaluation configs, or cost policies
- Additional log schema variants or telemetry instrumentation
- Documentation guides, walkthroughs, or usage clarifications
- Governance patterns, safety mechanisms, or policy modules

## How to Contribute

Before contributing:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear, documented commits
4. Submit a pull request with purpose, context, and reasoning

Need orientation? Start with the [Developer Integration Guide](docs/implementation/dev-guide.md) or [Repo Tour](docs/getting-started/repo-tour.md).

## What a Good PR Looks Like

Strong pull requests typically include:

1. **Purpose** — A clear explanation of what the PR changes and why
2. **Prompt Impact** — If modifying a prompt:
   - Update `prompt-card.example.yml` or applicable prompt card
   - Add an entry to `prompt-change-log.yml`
3. **Test Coverage** — Ensure test cases exist in:
   - `evals/test-cases.json`
   - `evals/prompt-injection-tests.json` (if relevant)
4. **CI Compliance** — Confirm `make eval` and `make test` pass
5. **Approval Workflows** — If updating a production prompt, include a HITL approval form under `/reviews/`

### Example PR Title and Description

**Title:** feat(prompt): update support-agent prompt for better cost control  
**Description:**

- Added fallback handling to avoid context explosion
- Reduced output verbosity to lower average tokens
- New version: v1.2.1
- Added test case: cost regression check
- HITL approval: included in `/reviews/support-agent-v1.2.1.md`

## Documentation Contributions

We encourage contributors to help improve onboarding and understanding:

- Fix unclear language or typos
- Add walkthroughs and explanations to the `docs/` directory
- Clarify governance terms or versioning examples
- Expand existing sections with patterns, use cases, or comparisons

Start with [docs/index.md](docs/index.md) or the [Quickstart section](docs/getting-started/what-is-promptops.md).

## File Ownership and Review Notes

Certain folders require additional care:

- `schemas/`, `prompts/`, `evals/` — Changes must preserve compatibility or include migration notes
- `ci/`, `scripts/`, `Makefile` — Must pass `make test` and `make eval`
- `docs/` — No approval required for small fixes; flag architectural changes in your PR

## Repository Structure Reference

For a complete overview of how the repository is structured and how components fit together, see:

- [REPO_MANIFEST.md](REPO_MANIFEST.md)

## Not Ready to Open a PR?

We still welcome feedback. You can:

- Open an issue with a bug, question, or idea
- Propose a governance pattern or integration challenge
- Share edge cases, drift scenarios, or evaluation methods

This artifact evolves through real-world usage. If something breaks or feels confusing, that’s valuable input.

## Usage and Licensing Terms

This repository is licensed under the [MIT License](LICENSE.txt). You are free to use, modify, and adapt it for internal and commercial purposes with attribution.

For enterprise integration, OEM redistribution, or commercial licensing inquiries, please contact the maintainer directly.

## Governance Alignment

This artifact is designed to support:

- Prompt versioning, rollback safety, and CI integration
- Evaluation pipelines for drift, cost, hallucination, and injection risk
- Multi-agent coordination with traceable logs and role schemas
- Reproducible governance aligned with standards like OWASP, SOC2, and NIST

Contributions that support or extend these governance goals are prioritized.

---

Thank you for helping strengthen the AI-native development ecosystem.
