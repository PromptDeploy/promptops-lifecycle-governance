# PromptOps Lifecycle Governance

> ⚠️ This repo is actively under development. Docs in progress - I’m writing walkthroughs for this artifact

Governance scaffolding for prompt versioning, eval gating, rollback flows, and observability — built for SaaS SDK teams deploying AI-native systems.

## Why This Exists

LLM-powered products are fragile. Prompt drift, eval regressions, agent failures, hallucinations, cost spikes — these are real problems for teams.

This repo installs a governance scaffold into your AI pipeline to help you:

- Version prompts like code
- Gate changes through CI evals
- Log every decision for auditability
- Mitigate multi-agent and RAG failures
- Align with OWASP and OpenTelemetry standards

Think of it as “Terraform for Prompts” — declarative, reproducible, and safe to scale.

## Who This Is For

This governance scaffold is built for:

- **SaaS SDK PMs** managing developer-facing LLM tools
- **Infra engineers** building LangChain-style frameworks, agents, or eval layers
- **LLM platform teams** integrating prompt pipelines into real workflows
- **Enterprise AI governance teams** enforcing prompt safety and reproducibility

## What’s Inside

| Layer                 | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| `schemas/`            | Prompt version schema, changelog format, prompt card metadata   |
| `evals/`              | Promptfoo configs, test cases (core, variants, RAG, comparison) |
| `logs/`               | Structured log formats, cost metrics schema                     |
| `ci/`                 | Eval gates, production enforcement rules                        |
| `workflows/`          | Promotion pipeline, rollback plan, approval templates           |
| `examples/`           | OWASP mapping, prompt cards, agent verification examples        |
| `integration-guides/` | LangChain, OpenAPI, Pinecone integration tips                   |
| `audit/`              | Failure mode catalog, log formats, HITL audit views             |
| `scripts/`            | CLI runner, prompt card dashboard generator                     |
| `tests/`              | Regression scenarios for different prompt types                 |
| `docs/`               | Developer overview and walkthroughs                             |

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
python scripts/prompt-eval-runner.py         # Non-strict preview mode
python scripts/prompt-eval-runner.py --strict  # Strict mode (CI-style)
```

## Prompt Eval Scenarios

### Standard Eval

```bash
promptfoo test --config evals/eval-config.promptfoo.yml
```

### Variant Prompt Eval

```bash
promptfoo test --config evals/eval-config.variant.promptfoo.yml
```

### Claude vs GPT Comparison

```bash
promptfoo test --config evals/eval-config.compare.promptfoo.yml
```

### RAG Fallback Behavior

```bash
promptfoo test --config evals/eval-config.rag.promptfoo.yml
```

> Tests for hallucination, weak context, and fallback phrasing

📄 Sample report: [`evals/eval-report.rag.md`](evals/eval-report.rag.md)

## Prompt Metadata & Dashboards

Your canonical prompt definition lives in:

- `schemas/prompt-card.example.yml` – full prompt metadata
- `schemas/prompt-card.dashboard.yml` – dashboard-friendly view

### Generate dashboard YAML from canonical source:

```bash
python scripts/generate-dashboard-card.py
```

> Syncs team-readable view for PMs, Notion, or Slack dashboards.

## Governance Features

- Prompt version schema + changelog tracking
- CI gate for eval regressions + schema violations
- Eval pipelines for Claude, GPT, variants, RAG
- Fallback logging for multi-agent + RAG failures
- Structured cost logs with OpenTelemetry-style schema
- Policy-as-code examples for CI, HITL, approval gating
- Audit log templates and OWASP LLM security mapping

## Minimal Working Lifecycle Example

Track the full lifecycle of `support-agent-v1`:

| Stage          | File                                                               |
| -------------- | ------------------------------------------------------------------ |
| Metadata       | `schemas/prompt-card.example.yml`                                  |
| Version Tags   | `schemas/prompt-version.prod-approved.yml`                         |
| Eval Config    | `evals/eval-config.promptfoo.yml`                                  |
| CI Gate        | `ci/ci-prod-block.yml`                                             |
| Logs & Output  | `logs/log-sample.output.json`, `logs/prompt-log-schema.json`       |
| Dashboard View | `schemas/prompt-card.dashboard.yml`                                |
| RAG Behavior   | `evals/test-cases.rag.json`, `evals/eval-config.rag.promptfoo.yml` |
| Eval Report    | `evals/eval-report.rag.md`                                         |

## Key Make Commands

```bash
make eval           # Run standard prompt evals (non-blocking)
make test           # Run governance evals and save results (CI-style)
make strict-eval    # Enforce CI thresholds on saved eval results
make logs           # View sample output logs

make inject-test    # Run prompt injection test cases for jailbreak coverage
make rag-eval       # Evaluate RAG fallback behavior (empty/vague context)

make dashboard      # Generate dashboard-friendly prompt card view
make format         # Format Python/YAML/JSON files (optional)
make lint           # (Optional) Run schema linter or CI sanity checks
```

## PromptOps Documentation

- [What Is PromptOps? A Practical Introduction](docs/intro-to-promptops.md)

## 📜 License & Remixing

This repo is built for reuse. You are encouraged to:

- Use it inside SDKs, R&D pipelines, or internal demos
- Remix schemas, scripts, tests, or CI flows
- Teach or present this framework with attribution
- Fork the repo — and send PRs if you extend it!

License: MIT for internal and educational use.

Commercial licensing is available for SDKs, cloud platforms, and enterprise teams.

[📧 kappainnovationllc@gmail.com](mailto:kappainnovationllc@gmail.com)

## Author

Built by a solo engineer learning the full governance stack — writing docs, running tests, and evolving this artifact in public.
→ [linkedin.com/in/houchia](https://linkedin.com/in/houchia)  
→ [prompt-deploy.beehiiv.com](https://prompt-deploy.beehiiv.com)

If this helps your team, I'd love to hear from you.

## Inspirations & Related Work

This artifact draws influence from:

- OpenTelemetry (for traceability)
- Promptfoo (for eval pipelines)
- Terraform (for declarative governance)
- OWASP LLM Top 10 (for risk coverage)

## Final Notes

- Supports Promptfoo, LangChain, OpenAPI, Pinecone pipelines
- Compliant with OWASP LLM Top 10
- Extendable to Claude, GPT, and open-source providers

For governance-grade prompt infrastructure — this is your starting scaffold.

## Learn More

- [Agent Governance Guide](docs/agent-governance.md)
- [Developer Walkthrough](docs/dev-guide.md)
- [PromptOps FAQ](docs/faqs.md)
