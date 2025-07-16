# Integration Guides

This folder contains SDK-specific integration guides to help platform teams embed PromptOps governance scaffolds into their existing LLM infrastructure.

These guides are designed for:

- SaaS platform teams (LangChain, OpenDevin, CrewAI, etc.)
- Infra engineers integrating evaluation or logging layers
- Developer tooling teams building prompt pipelines, agent flows, or orchestration graphs

Each guide shows how to adopt PromptOps components (schemas, evals, logs, versioning) within real-world SDK surfaces.

## File Index

| File                                               | Description                                                                                     |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [`langchain.md`](./langchain.md)                   | Overview of how to plug PromptOps into LangChain prompt templates and chains                    |
| [`langchain-snippets.py`](./langchain-snippets.py) | Code snippets for integrating PromptOps versioning, logging, and evals into LangChain workflows |
| [`openapi-agent.md`](./openapi-agent.md)           | Guide for aligning OpenAPI agents with PromptOps fallback and prompt governance layers          |
| [`pinecone.md`](./pinecone.md)                     | Notes on integrating vector DB indexing + PromptOps logging/rollback into RAG flows             |

## Usage

Use these guides when:

- Embedding prompt lifecycle governance into your SDK
- Designing evaluation-aware prompt interfaces
- Supporting multi-agent orchestration with auditability and rollback
- Replacing ad hoc prompt use with reproducible, testable, version-controlled flows

These are meant to be extended — fork, adapt, and integrate them into your internal SDK documentation or onboarding playbooks.
