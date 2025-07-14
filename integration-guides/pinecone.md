# Pinecone Integration Guide

This guide shows how to integrate the PromptOps governance scaffolds into a Pinecone-powered RAG (Retrieval-Augmented Generation) pipeline. It assumes you are using a vector database to retrieve context chunks and applying prompts for synthesis, QA, or reasoning.

---

## Use Case

You operate a support bot that:

1. Receives a question
2. Retrieves documents from Pinecone
3. Injects context into a versioned prompt
4. Generates an answer via LLM
5. Logs all relevant telemetry for audit and rollback

---

## Integration Steps

### 1. Version Your Prompt

Store prompt templates that perform context injection and synthesis under version control:

```yaml
name: "rag_support_synth"
version: "v1.0.0"
template: |
  Use the context below to answer the customer’s question. If you don’t know, say “I don’t know”.

  Context:
  {{context}}

  Question:
  {{question}}

  Answer:
variables:
  - context
  - question
```

Track it in `schemas/prompt-version-schema.yml` and changes in `schemas/prompt-change-log.yml`.

---

### 2. Retrieve Context from Pinecone

```python
from langchain.vectorstores import Pinecone
retriever = Pinecone.from_existing_index("support-docs-index", embeddings).as_retriever()
docs = retriever.get_relevant_documents(question)
context = "\n\n".join([doc.page_content for doc in docs])
```

---

### 3. Run Prompt

Format with retrieved context and feed into your LLM:

```python
from my_promptops_lib import load_prompt_version
template = load_prompt_version("rag_support_synth", version="v1.0.0")
output = llm.run(template.format(context=context, question=question))
```

---

### 4. Log Prompt Execution

```json
{
  "trace_id": "def-456",
  "prompt_id": "rag_support_synth",
  "version": "v1.0.0",
  "retrieved_chunks": 6,
  "tokens_used": 193,
  "output": "Please restart your app...",
  "timestamp": "2025-07-01T11:00:00Z",
  "context_hash": "ae9f...432"
}
```

Log to JSONL file and validate against `logs/prompt-log-schema.json`.

---

### 5. Evaluate Prompt Before Promotion

Run tests from `evals/test-cases.json` for:

- Context fidelity
- Hallucination rate
- Latency and cost

Use Promptfoo YAML config and CI eval gate (`ci/eval-gate.yml`).

---

## Governance Benefits

- Ensure retrieved content is used responsibly
- Track which docs led to which answers
- Validate prompt behavior before every deployment
- Trace version-to-output regressions

---

## Related Files

- [`schemas/prompt-version-schema.yml`](../schemas/prompt-version-schema.yml)
- [`logs/prompt-log-schema.json`](../logs/prompt-log-schema.json)
- [`examples/rag-pipeline-lifecycle.md`](../examples/rag-pipeline-lifecycle.md)
- [`evals/test-cases.json`](../evals/test-cases.json)
- [`ci/eval-gate.yml`](../ci/eval-gate.yml)

---

> Last updated: 2025-07-14
