# LangChain Integration Guide

This guide shows how to integrate PromptOps governance scaffolds into LangChain workflows.

---

## Use Case: Chain with ReAct-style Planning

LangChain developers often build chains with multiple prompt templates and agents.

Common issues:

- Prompts change without audit logs
- Evaluation is ad-hoc or missing
- No way to rollback when a change degrades accuracy

---

## Integration Flow

1. **Prompt Versioning**

Use versioned prompts from `schemas/prompt-version-schema.yml`.  
Example field: `"planner_v1.2.0"`  
Reference it explicitly when building a `PromptTemplate`:

```python
PromptTemplate.from_template(
    template=versioned_prompt["template"],
    input_variables=versioned_prompt["vars"]
)
```

2. **Evaluation Gating (Optional)**

Use Promptfoo config (`evals/eval-config.promptfoo.yml`) to validate prompt before merging.

Run this locally or in CI:

```bash
promptfoo test -c evals/eval-config.promptfoo.yml
```

3. **Logging Prompt Inputs + Outputs**

Import the `prompt-log-schema.json` format and log fields:

- prompt_id
- model
- trace_id
- cost estimate

Hook into LangChain’s `callback_manager` to trace:

```python
from langchain.callbacks import StdOutCallbackHandler
from promptops.logger import PromptLogger

logger = PromptLogger(schema_path="logs/prompt-log-schema.json")
handler = StdOutCallbackHandler()

# Attach handler to chain
chain.callback_manager.add_handler(handler)
```

4. **Rollback Support**

Use versioning and `rollback-flow.md` guidance to revert to prior known-good prompt if eval fails.

---

## Test Run

```bash
python scripts/prompt-eval-runner.py \
  --prompt_id planner_v1.2.0 \
  --input '{"task": "Summarize this report"}'
```

---

## Related Files

- [`schemas/prompt-version-schema.yml`](../../schemas/prompt-version-schema.yml)
- [`logs/prompt-log-schema.json`](../../logs/prompt-log-schema.json)
- [`ci/eval-gate.yml`](../../ci/eval-gate.yml)
- [`scripts/prompt-eval-runner.py`](../../scripts/prompt-eval-runner.py)

---

> Last updated: 2025-07-14
