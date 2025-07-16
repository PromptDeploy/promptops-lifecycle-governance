# Logging Agent Prompts (Nested Format)

For teams using LangGraph, CrewAI, ReAct agents, or prompt chains — the PromptOps artifact supports **nested agent traces**.

Use the `log-schema-v2.json` to capture:

- Step-by-step tool usage (e.g. search, lookup, summarize)
- Agent reasoning at each step
- Cost and token counts per operation
- Final synthesized output and total cost

## Files

- `schemas/log-schema-v2.json` – JSON Schema for nested agent logs
- `logs/agent-log.example.json` – Valid example using Claude-3 with 2 steps

## Use Case

| Scenario                     | What to Log                                        |
| ---------------------------- | -------------------------------------------------- |
| LangChain agents             | Each prompt call + tool use as a `step`            |
| Retrieval + synthesis chains | Separate retrieval and response steps              |
| Claude tool-use mode         | Reasoning, tool output, final result per tool call |

## CI/Policy Tip

Use agent logs for:

- Manual or automated audits
- Cost-based rollback triggers
- Explaining “why did the agent do that?”
