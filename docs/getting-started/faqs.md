# FAQ's: PromptOps Lifecycle Governance

This artifact is designed for governance-grade prompt versioning, evaluation, and rollback. But like any dev-facing system, it must stand up to engineering scrutiny. This doc surfaces common objections engineers may have.

## ❌ “Why do we need prompt versioning? Git already versions everything.”

Git doesn’t capture:

- Prompt approval state
- Eval pass/fail status
- Cost risk
- Production vs staging context

This artifact tracks prompt _behavior_ — not just file diffs. Think: semantic versioning, human approval, eval compliance.

## ❌ “Promptfoo isn't the industry standard — why use it?”

Promptfoo is a reference implementation. The artifact is model-agnostic — swap in LangSmith, Guardrails, or Claude CLI outputs. Promptfoo helps prove CI integration and local testability.

## ❌ “Too much ceremony. Just want to test prompts fast.”

Use the `minimal/` setup:

- One schema
- One eval test
- One log

Governs the most critical risk: silent regression.

## ❌ “This doesn’t support agents or RAG.”

True — this artifact governs **individual prompts**. It’s composable across:

- Agent nodes (LangGraph)
- Retrieval chains (LlamaIndex, Pinecone)

Agent and RAG-specific governance lives in future artifacts (e.g. Debugging Copilot, Agent Design Matrix).

## ❌ “How do I integrate this into my existing repo?”

Use `docs/integration-guide.md` (coming soon):

- LangChain: version + test your prompt node
- Cursor: use log schema + HITL tags for prompt panels
- Claude: track eval pass/fail across versions

## ❌ “This is too GPT/Claude specific.”

Prompt evaluation is model-agnostic. We've tested with:

- GPT-4 / Claude / Cohere / Ollama
- Any API-returning model is supported
- Add your provider config in `evalsuite-core-config.yml`

## ❌ “No enforcement — devs can ignore the schema.”

CI gates (`ci/eval-gate.yml`) enforce:

- Promptfoo eval thresholds
- Schema validity
- Prompt log presence
- Approval field checks

Hard-mode branches include pre-merge guards and PR blockers.

## ❌ “Rollback sounds manual.”

Yes — rollback is traceable, not magic. It includes:

- Restoring eval-passing prompt
- Updating schema version
- Triggering new eval run
- Logging the rollback decision

## ❌ “We move too fast for this kind of governance.”

Use governance modes:

- 🟢 **Fast team:** 1 schema + 1 eval
- 🟡 **Growing org:** CI eval + version tags
- 🔴 **Governed org:** Approval + rollback + audit trail

## ❌ “We use LangSmith already — isn’t that enough?”

LangSmith is great for tracing — this artifact adds **version enforcement**, **CI gating**, and **structured rollback triggers**.

Use LangSmith for UI traceability, PromptOps for lifecycle control.

## ❌ “Where do we store the logs?”

Logs are schema-bound JSON. Store locally, in S3, or pipe to OpenTelemetry-compatible systems.

Schema: [`schemas/prompt-log-schema.json`](../schemas/prompt-log-schema.json)

## ❌ “Too much config. Can't we just hardcode prompts?”

You can — but you lose:

- Drift detection
- Cost awareness
- Approval history
- CI enforcement

This artifact separates prompt _intent_ (the YAML) from _execution_ (the LLM call).

## ❌ “What if my team just ignores this?”

PromptOps is opt-in — but CI hooks, approval tags, and eval gates make non-compliance visible.

Start with the `minimal/` path and build trust through automation, not mandates.

---

## Want to Help?

Clone the starter repo, remix an eval config, or file a GitHub issue with a real objection. We’ll test it, log it, and ship a fix.
