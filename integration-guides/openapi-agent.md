# OpenAPI Agent Integration Guide

This guide shows how to integrate PromptOps governance scaffolds into agent systems that interact with OpenAPI-based tools. It is tool-agnostic and applies to any agent framework (custom-built, LangChain, AutoGen, etc.) that calls external APIs using prompt-driven logic.

---

## Use Case

You’re deploying a support agent that:

- Parses user input
- Uses a versioned prompt to decide on action
- Calls a third-party OpenAPI (e.g., CRM or ticket system)
- Logs all prompt decisions and results for audit and rollback

---

## Key Governance Hooks

| Concern                | How to Handle It                           | PromptOps File                      |
| ---------------------- | ------------------------------------------ | ----------------------------------- |
| Prompt version control | Use versioned prompt metadata              | `schemas/prompt-version-schema.yml` |
| Prompt audit log       | Track prompt ID, input, output, API result | `schemas/prompt-log-schema.json`    |
| Cost visibility        | Token + API cost logging                   | `logs/cost-metrics-schema.yml`      |
| Eval before deployment | Run Promptfoo tests                        | `evals/evalsuite-core-config.yml`   |
| Rollback faulty logic  | Follow rollback procedure                  | `workflows/rollback-flow.md`        |

---

## Sample Integration Steps

### 1. Define your agent’s action prompt

```yaml
name: "resolve_customer_ticket"
version: "v1.0.3"
template: |
  Given the following customer message, determine if we should:
  - Escalate to engineering
  - Create a support ticket
  - Request clarification

  Respond ONLY with the action: "escalate", "ticket", or "clarify".

  Message: {{customer_message}}
variables:
  - customer_message
```

Store this as a versioned prompt with metadata in `schemas/`.

---

### 2. Use it in your agent code

Inject versioned prompt via variable map (`{{customer_message}}`) and call the LLM.

```python
from my_promptops_lib import load_prompt_version
prompt_template = load_prompt_version("resolve_customer_ticket", version="v1.0.3")
response = llm.run(prompt_template.format(customer_message=user_input))
```

---

### 3. Log the prompt run

```json
{
  "trace_id": "abc-123",
  "timestamp": "2025-07-01T10:00:00Z",
  "prompt_id": "resolve_customer_ticket",
  "version": "v1.0.3",
  "input": { "customer_message": "My app keeps crashing." },
  "output": "escalate",
  "tokens": 111,
  "api_calls": [
    {
      "name": "POST /escalate",
      "response_status": 200,
      "response_time_ms": 102,
      "cost_usd": 0.0012
    }
  ]
}
```

---

### 4. Run evals before promotion

Use `evals/test-cases.json` to check for unsafe outputs, hallucinations, or routing errors before deploying.

---

## 🔐 Governance Benefits

- Centralized visibility of agent behavior
- Traceable prompt logic + API behavior
- Reproducible regression tests
- Safer API orchestration
- Rollback-ready agent logic

---

## 🧠 Related Files

- [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml)
- [`schemas/prompt-log-schema.json`](../schemas/prompt-log-schema.json)
- [`evals/evalsuite-core-config.yml`](../evals/evalsuite-core-config.yml)
- [`workflows/rollback-flow.md`](../workflows/rollback-flow.md)

---

> Last updated: 2025-07-14
