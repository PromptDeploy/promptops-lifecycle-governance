# Prompt Eval Gating in CI

This example shows how to integrate evaluation gating into your CI pipeline using this artifact’s scaffolds.

---

## Scenario

You're updating a prompt used in your SaaS chatbot. You want to ensure:

- It doesn’t increase hallucination rate
- It keeps cost per completion under $0.002
- It passes 90%+ on known regression test cases

---

## File Highlights

- [`evals/eval-config.promptfoo.yml`](../../evals/eval-config.promptfoo.yml) — declares eval criteria
- [`evals/test-cases.json`](../../evals/test-cases.json) — includes test inputs + expected completions
- [`evals/cost-checks.yml`](../../evals/cost-checks.yml) — ensures token cost stays predictable
- [`ci/eval-gate.yml`](../../ci/eval-gate.yml) — CI workflow that fails builds on eval regressions

---

## How It Works

1. **Dev updates a prompt**
2. [`scripts/prompt-eval-runner.py`](../../scripts/prompt-eval-runner.py) runs Promptfoo tests in CI
3. Eval results are logged to [`logs/`](../../logs/)
4. [`ci/eval-gate.yml`](../../ci/eval-gate.yml) blocks merge if:
   - Accuracy drops below threshold
   - Cost spike exceeds policy
   - Safety criteria fails (e.g. toxicity)

---

## Example Output

✅ Passed: 7/8 test cases
📉 Accuracy: 88.5% (threshold = 90%)
💰 Estimated cost per prompt: $0.0017
⛔️ Merge blocked: accuracy below threshold

---

## GitHub Actions Flow

See [`ci/eval-gate.yml`](../../ci/eval-gate.yml) for implementation.

```yaml
# ci/eval-gate.yml (excerpt)
- name: Run prompt evaluations
  run: python scripts/prompt-eval-runner.py --config evals/eval-config.promptfoo.yml
```

---

## Benefits

- Prevents prompt regressions from reaching production
- Catches runaway cost increases
- Improves safety and reliability of LLM output
- SOC2 / OWASP-aligned prompt QA practice

## See Also

- evals/test-cases.json
- scripts/prompt-eval-runner.py
- ci/eval-gate.yml
