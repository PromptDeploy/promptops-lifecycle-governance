# PromptOps for Agent Chains: Version, Log, and Gate Every Role

PromptOps introduces nested agent logging, making it possible to govern and debug multi-step reasoning flows from tools like LangChain, Claude, CrewAI, ReAct-style agents, and more.

This doc shows how to:

- Structure agent logs using `agenttrace-schema.json.json`
- Capture reasoning, tool use, and cost per step
- Use logs for auditing, cost control, and rollback

This guide complements the main [README](../README.md) and [dev guide](./dev-guide.md).

→ You can compare agent output between Claude and GPT using [`eval-config.compare.promptfoo.yml`](../evals/eval-config.compare.promptfoo.yml).

---

## Required Files

| File                                  | Purpose                                    |
| ------------------------------------- | ------------------------------------------ |
| `schemas/agenttrace-schema.json.json` | Validates nested logs                      |
| `logs/agent-log.example.json`         | Example log from Claude agent              |
| `ci/eval-gate.yml`                    | Optional: Add approval enforcement logic   |
| `prompt-version-schema.yml`           | Link logs to versions + approval decisions |

---

## Agent Trace Format

Each step in the agent’s execution is recorded with:

- `step_number`: Order of execution
- `tool_call`: What tool or function the agent invoked
- `observation`: What the tool returned
- `reasoning`: Why the agent made that choice
- `output_tokens` + `cost_usd`: Optional for observability

Final output is captured under `agent_trace.final_output`.

---

## Auditing Use Cases

| Use Case                           | What to Log                        |
| ---------------------------------- | ---------------------------------- |
| Claude or GPT-4 agent using tools  | Each tool step and reasoning       |
| LangChain `RunnableSequence` agent | Log each node/tool step            |
| RAG + summarizer                   | Retrieval → synthesis in two steps |

---

## Rollback & Approval Flow

- Use `environment: prod` in `prompt-version-schema.yml`
- CI can block if no approval metadata is attached
- Optional: Rollback if final output fails eval or cost spikes

```yml
rollback_conditions:
  - "agent_trace.final_output fails hallucination eval"
  - "total_cost_usd > baseline + 20%"
```

---

## Future Features (Planned)

- Per-step eval scoring (Promptfoo integration)
- Prompt dashboard showing step-wise agent reasoning
- Cost-Risk overlays to flag high-cost prompt routes

---

## Resources

- [agenttrace-schema.json.json](../schemas/agenttrace-schema.json.json)
- [agent-log.example.json](../logs/agent-log.example.json)
- [PromptOps Objection Handling](../PROMPTOPS_OBJECTION_HANDLING.md)
