
import yaml
from pathlib import Path

def generate_dashboard_card(source_path, output_path):
    with open(source_path) as f:
        full_card = yaml.safe_load(f)

    card_data = full_card.get("prompt_card", {})

    dashboard_card = {
        "prompt_id": card_data.get("id"),
        "name": card_data.get("name"),
        "version": card_data.get("version"),
        "status": card_data.get("status"),
        "environment": card_data.get("environment"),
        "author": card_data.get("author"),
        "created_at": card_data.get("created_at"),
        "tags": card_data.get("tags"),
        "use_case": card_data.get("use_case"),
        "description": card_data.get("description"),
        "eval_metrics": {
            "criteria": [c["name"] for c in card_data.get("evaluation_criteria", [])],
            "rollback_if": card_data.get("rollback_conditions", []),
        },
        "related_files": card_data.get("related_artifacts", []),
        "notes": card_data.get("notes"),
    }

    with open(output_path, "w") as f:
        yaml.dump(dashboard_card, f, sort_keys=False)

    print(f"✅ Dashboard prompt card saved to: {output_path}")

if __name__ == "__main__":
    canonical_file = "schemas/prompt-card.example.yml"
    output_file = "schemas/prompt-card.dashboard.yml"
    generate_dashboard_card(canonical_file, output_file)
