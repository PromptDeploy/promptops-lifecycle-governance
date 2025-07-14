
# 📦 PromptOps Lifecycle Governance Makefile

# Core evaluations
eval:
	promptfoo test --config evals/eval-config.promptfoo.yml

test:
	promptfoo evaluate --config evals/eval-config.promptfoo.yml --output evals/.ci-eval-results.json
	python scripts/prompt-eval-runner.py --strict

strict-eval:
	python scripts/prompt-eval-runner.py --strict

logs:
	cat logs/log-sample.output.json | jq .

# New: Dashboard YAML sync
dashboard:
	python scripts/generate-dashboard-card.py

# New: Prompt injection test runner
inject-test:
	promptfoo test --config evals/eval-config.promptfoo.yml --tests evals/prompt-injection-tests.json

# New: RAG fallback test
rag-eval:
	promptfoo test --config evals/eval-config.rag.promptfoo.yml

# Optional: YAML/JSON formatting (requires jq/yq/pyyaml pre-installed)
format:
	black scripts/*.py
	yq -i evals/*.yml
	jq . logs/*.json > /dev/null

# Optional: schema linting or test validator
lint:
	echo "TODO: Add schema linting if needed"
