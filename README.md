# PromptOps Lifecycle Governance

**Status:** v0.1.0 · Docs in progress · MIT licensed

Governance scaffolding for prompt versioning, eval gating, rollback flows, and observability — built for SaaS SDK teams deploying AI-native systems.

## Why This Exists

LLM-powered products are fragile.

Prompt drift, eval regressions, agent failures, hallucinations, cost spikes — these are real problems.

This repo installs a governance scaffold into your AI pipeline to help you:

- Version prompts like code
- Gate changes through CI evals
- Log every decision for auditability
- Mitigate multi-agent and RAG failures
- Align with OWASP and OpenTelemetry standards

Think of it as **“Terraform for Prompts”** — declarative, reproducible, and safe to scale.

## Who This Is For

This governance scaffold is designed for:

- **SaaS SDK PMs** — managing developer-facing LLM tools
- **Infra engineers** — building LangChain-style frameworks, agents, or eval layers
- **LLM platform teams** — integrating prompt pipelines into real workflows
- **AI governance teams** — enforcing prompt safety, reproducibility, and audit trails

## What’s Inside

| Layer                 | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| `schemas/`            | Prompt version schema, changelogs, canonical metadata            |
| `evals/`              | Promptfoo configs, test cases (core, variants, RAG, comparison)  |
| `logs/`               | Structured logging, cost metrics schema, observability formats   |
| `ci/`                 | Eval gates, production enforcement rules                         |
| `workflows/`          | Promotion pipelines, rollback flow, HITL approval templates      |
| `examples/`           | OWASP mapping, agent verification chains, lifecycle walkthroughs |
| `integration-guides/` | LangChain, OpenAPI, Pinecone integration patterns                |
| `audit/`              | Failure mode catalog, compliance mapping, audit trail templates  |
| `scripts/`            | CLI runners, prompt card dashboard generators                    |
| `tests/`              | Regression scenarios for various prompt behaviors                |
| `docs/`               | Full walkthroughs and role-specific documentation                |

## Quickstart

```bash
git clone https://github.com/yourname/promptops-lifecycle-governance.git
cd promptops-lifecycle-governance
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

make test  # Run governance eval with CI thresholds
```

Or run standalone:

```bash
python scripts/prompt-eval-runner.py         # Preview mode
python scripts/prompt-eval-runner.py --strict  # CI enforcement
```

## Walkthroughs & Docs

- [What Is PromptOps?](docs/getting-started/what-is-promptops.md)
- [PromptOps FAQ](docs/getting-started/faqs.md)
- [Developer Integration Guide](docs/implementation/dev-guide.md)
- [Agent Governance Guide](docs/governance/agent-governance.md)
- [Full Docs Index →](docs/index.md)

---

## Key Make Commands

**Eval & Test**

- `make eval` — Run prompt evals
- `make test` — Run governance evals + CI checks
- `make inject-test`, `make rag-eval` — Run edge-case eval suites

**Dashboards & Logs**

- `make dashboard` — Generate PM-friendly dashboard YAML
- `make logs` — View sample output logs

**Tooling**

- `make format`, `make lint` — Optional formatting/linting

## License & Remixing

This repo is built for reuse.

You are encouraged to:

- Integrate this scaffold into SDKs, infra stacks, or platform tools
- Fork, remix, and extend evals, changelogs, CI gates, and audit tools
- Use this as a governance baseline for internal or regulated deployments

License: [MIT](./LICENSE.txt) (internal and educational use).
Commercial licensing available for SDKs, platform integrations, and enterprise systems.

Contact: [kappainnovationllc@gmail.com](mailto:kappainnovationllc@gmail.com)

## Author

Built by [Hou Chia](https://linkedin.com/in/houchia) — a solo engineer designing governance scaffolds for AI-native teams.

See ongoing builds: [prompt-deploy.beehiiv.com](https://prompt-deploy.beehiiv.com)

## Inspirations

This artifact draws on patterns from:

- **Promptfoo** – for prompt evaluation pipelines
- **OpenTelemetry** – for traceable logs and cost observability
- **Terraform** – for declarative, auditable workflows
- **OWASP LLM Top 10** – for safety and risk mitigation

---

## Compliance & Extensibility

- Compliant with OWASP LLM Top 10
- Supports Promptfoo, LangChain, Pinecone, OpenAPI pipelines
- Extendable to Claude, GPT, and open-source models

For governance-grade prompt infrastructure — this is your installable starting point.
