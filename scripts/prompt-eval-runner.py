import json
import subprocess
import sys
import argparse
from pathlib import Path

# Thresholds
THRESHOLDS = {
    "min_score": 0.85,
    "min_pass_rate": 0.90
}

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Paths
EVAL_CONFIG = Path("evals/eval-config.promptfoo.yml")
TEST_CASES = Path("evals/test-cases.json")

def run_promptfoo(strict=False):
    print("🚀 Running Promptfoo evaluations...\n")

    if not EVAL_CONFIG.exists():
        print(f"{RED}❌ Missing eval config: {EVAL_CONFIG}{RESET}")
        sys.exit(1)

    if not TEST_CASES.exists():
        print(f"{RED}❌ Missing test cases: {TEST_CASES}{RESET}")
        sys.exit(1)

    cmd = [
        "promptfoo", "test",
        "--config", str(EVAL_CONFIG),
        "--tests", str(TEST_CASES),
        "--output", "json"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{RED}❌ promptfoo test failed to run.{RESET}")
        print(e.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{RED}❌ Failed to parse promptfoo output as JSON.{RESET}")
        sys.exit(1)

    # Validate output
    results = data.get("results", [])
    if not results:
        print(f"{RED}❌ No eval results found.{RESET}")
        sys.exit(1)

    passed = sum(1 for r in results if r.get("pass") is True)
    scores = [r.get("score", 0) for r in results if "score" in r]

    avg_score = sum(scores) / len(scores) if scores else 0
    pass_rate = passed / len(results)

    print("📊 Promptfoo Eval Summary")
    print(f"{GREEN if pass_rate >= THRESHOLDS['min_pass_rate'] else RED}✓ Pass Rate: {pass_rate:.2%}{RESET}")
    print(f"{GREEN if avg_score >= THRESHOLDS['min_score'] else RED}✓ Avg Score: {avg_score:.2f}{RESET}")

    if strict:
        if pass_rate < THRESHOLDS["min_pass_rate"]:
            print(f"{RED}❌ Fail: Pass rate below threshold ({pass_rate:.2%} < {THRESHOLDS['min_pass_rate']:.0%}){RESET}")
            sys.exit(1)

        if avg_score < THRESHOLDS["min_score"]:
            print(f"{RED}❌ Fail: Avg score below threshold ({avg_score:.2f} < {THRESHOLDS['min_score']}){RESET}")
            sys.exit(1)

        print(f"{GREEN}✅ All thresholds passed (strict mode).{RESET}")
    else:
        print(f"{YELLOW}⚠️ Eval complete (non-strict mode). Thresholds not enforced.{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run promptfoo evals with governance thresholds.")
    parser.add_argument("--strict", action="store_true", help="Enforce threshold failure exit")
    args = parser.parse_args()

    run_promptfoo(strict=args.strict)
