import json
from collections import defaultdict
from pathlib import Path
import pandas as pd

LOG_PATH = Path("logs/log-sample.output.json")

def load_logs(path):
    if not path.exists():
        raise FileNotFoundError(f"Missing log file: {path}")
    with open(path, "r") as f:
        return json.load(f)

def summarize_costs(logs):
    summary = defaultdict(lambda: {"count": 0, "total_tokens": 0, "total_cost": 0.0})
    for entry in logs:
        name = entry.get("prompt_name", "unknown")
        model = entry.get("model", "unknown")
        cost = float(entry.get("cost_usd", 0))
        tokens = int(entry.get("token_count", 0))

        summary[(name, model)]["count"] += 1
        summary[(name, model)]["total_tokens"] += tokens
        summary[(name, model)]["total_cost"] += cost

    records = []
    for (name, model), stats in summary.items():
        avg_cost = stats["total_cost"] / stats["count"]
        avg_tokens = stats["total_tokens"] / stats["count"]
        records.append({
            "Prompt": name,
            "Model": model,
            "Eval Count": stats["count"],
            "Avg Tokens": round(avg_tokens, 1),
            "Avg Cost (USD)": round(avg_cost, 4),
            "Total Cost (USD)": round(stats["total_cost"], 4)
        })
    return pd.DataFrame(records)

def main():
    logs = load_logs(LOG_PATH)
    df = summarize_costs(logs)
    output_file = Path("logs/cost-dashboard.csv")
    df.to_csv(output_file, index=False)
    print(f"✅ Cost dashboard saved to: {output_file}")

if __name__ == "__main__":
    main()
