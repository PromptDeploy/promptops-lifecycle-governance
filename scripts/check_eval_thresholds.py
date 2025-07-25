import json
import sys

THRESHOLDS = {
    "min_score": 0.85,
    "min_pass_rate": 0.90
}

def main(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"::error:: Failed to read eval results: {e}")
        sys.exit(1)

    if "results" not in data or not isinstance(data["results"], list):
        print("::error:: Invalid Promptfoo results format.")
        sys.exit(1)

    total = len(data["results"])
    if total == 0:
        print("::error:: No test cases found in eval results.")
        sys.exit(1)

    passed = sum(1 for r in data["results"] if r.get("pass") is True)
    scores = [r.get("score", 0) for r in data["results"] if isinstance(r.get("score", None), (int, float))]

    avg_score = sum(scores) / len(scores) if scores else 0
    pass_rate = passed / total

    print(f"Promptfoo Eval Report:")
    print(f"  ✓ Pass Rate: {pass_rate:.2%}")
    print(f"  ✓ Avg Score: {avg_score:.2f}")

    if pass_rate < THRESHOLDS["min_pass_rate"]:
        print(f"::error:: Pass rate below threshold ({pass_rate:.2%} < {THRESHOLDS['min_pass_rate']:.0%})")
        sys.exit(1)

    if avg_score < THRESHOLDS["min_score"]:
        print(f"::error:: Avg score below threshold ({avg_score:.2f} < {THRESHOLDS['min_score']})")
        sys.exit(1)

    print("::notice:: All evaluation thresholds passed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check-eval-thresholds.py <path_to_promptfoo_output.json>")
        sys.exit(1)

    main(sys.argv[1])
