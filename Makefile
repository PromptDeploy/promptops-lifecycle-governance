# 📦 PromptOps Lifecycle Governance Makefile

# Core evaluation pipeline (requires .env + promptfoo + API keys)
eval:
	npm run eval

test:
	npm run test

# make eval-prompt prompt=support-agent-v1
eval-prompt:
	npm run test:prompt -- $(prompt)

strict-eval:
	npm run strict-eval

logs:
	cat logs/log-sample.output.json | jq .

# Dashboard YAML sync
dashboard:
	python scripts/generate-dashboard-card.py

# Prompt injection test runner
inject-test:
	npx promptfoo test --config evals/evalsuite-core-config.yml --tests evals/prompt-injection-tests.json

# RAG fallback test
rag-eval:
	npx promptfoo test --config evals/eval-config.rag.promptfoo.yml

# Optional: YAML/JSON formatting (requires jq/yq/pyyaml pre-installed)
format:
	black scripts/*.py
	yq -i evals/*.yml
	jq . logs/*.json > /dev/null

lint-prompts:
	npx tsx scripts/lint-prompts.ts
