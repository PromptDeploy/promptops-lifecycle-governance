# Cost Metrics Dashboard: Visualize Token Spend and Inference ROI

Track token usage, cost risk thresholds, and monthly inference budget trends.

---

## Prompt Cost Summary

| Prompt Name         | Version | Avg Tokens | Avg Cost (USD) | Provider  | Model    | Last Eval  |
| ------------------- | ------- | ---------- | -------------- | --------- | -------- | ---------- |
| support-agent-v1    | v1.2.0  | 245        | $0.0021        | OpenAI    | gpt-4    | 2025-07-01 |
| rag-fallback-prompt | v1.0.3  | 415        | $0.0038        | Anthropic | claude-3 | 2025-06-27 |

> Data pulled from: `logs/log-sample.output.json`

---

## Monthly Cost Breakdown

| Month   | Total Prompts | Total Tokens | Total Cost (USD) |
| ------- | ------------- | ------------ | ---------------- |
| 2025-06 | 1,214         | 252,500      | $13.08           |
| 2025-07 | 928           | 188,960      | $10.44           |

---

## Risk Thresholds

| Metric                      | Threshold      | Status   |
| --------------------------- | -------------- | -------- |
| Avg cost per prompt         | ≤ $0.005       | ✅ Pass  |
| Cost spike (week-over-week) | ≤ 25% increase | ⚠️ 19% ↑ |
| Toxicity eval budget share  | ≤ 5% of total  | ✅ 3.2%  |
| Long-context usage share    | ≤ 10%          | ❌ 13.7% |

---

## Actions & Anomalies

- [ ] Cost spike from v1.1.1 → v1.2.0 identified
- [ ] Long-context usage optimizations pending
- [ ] Suggest moving `gpt-4` evals to `gpt-3.5` for drafts

---

## Data Sources

- `logs/prompt-log-schema.json`
- `logs/log-sample.output.json`
- `evals/eval-config.promptfoo.yml`
- `cost-checks.yml`

---

## Tips

- Use `jq` or `pandas` to generate this report automatically each month.
- Automation script: `scripts/generate-cost-dashboard.py`.
