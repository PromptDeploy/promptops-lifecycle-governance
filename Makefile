# 📦 PromptOps Lifecycle Governance Makefile

# Core evaluations
eval:
	npx promptfoo test --config evals/evalsuite-core-config.yml

test:
	npx promptfoo evaluate --config evals/evalsuite-core-config.yml --output evals/.ci-eval-results.json
	python scripts/prompt-eval-runner.py --strict

strict-eval:
	python scripts/prompt-eval-runner.py --strict

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

# Optional: schema linting or test validator
lint:
	echo "TODO: Add schema linting if needed"
