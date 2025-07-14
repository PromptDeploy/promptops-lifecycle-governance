from pathlib import Path

# Define the Python snippets content
langchain_snippets_content = """# langchain-snippets.py
\"\"\"
Reusable LangChain integration snippets for PromptOps governance artifact.
Includes:
- Prompt version loading
- Prompt logging with schema
- Evaluation integration
- Rollback logic placeholder
\"\"\"

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StdOutCallbackHandler
import uuid
import datetime
import json

# ---- Load versioned prompt ----
def load_prompt(version_id):
    # In practice, load this from version-controlled schema or DB
    versioned_prompt = {
        "id": version_id,
        "template": "You are a helpful assistant. Answer clearly: {{question}}",
        "vars": ["question"]
    }
    return PromptTemplate.from_template(
        template=versioned_prompt["template"],
        input_variables=versioned_prompt["vars"]
    )

# ---- Initialize logger ----
def log_prompt_run(prompt_id, input_vars, output_text, cost_tokens):
    log_entry = {
        "trace_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "prompt_id": prompt_id,
        "input": input_vars,
        "output": output_text,
        "tokens_used": cost_tokens,
        "estimated_cost_usd": round(cost_tokens * 0.000002, 6)  # dummy estimate
    }
    with open("logs/prompt_run_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\\n")

# ---- Run prompt ----
def run_prompt():
    prompt_id = "planner_v1.2.0"
    prompt = load_prompt(prompt_id)
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    chain = LLMChain(prompt=prompt, llm=llm)

    input_data = {"question": "What is prompt governance?"}
    result = chain.run(input_data)

    # Log with fake token cost
    log_prompt_run(prompt_id, input_data, result, cost_tokens=125)

    print("Output:", result)

if __name__ == "__main__":
    run_prompt()
"""

# Write the file
file_path = Path("/mnt/data/langchain-snippets.py")
file_path.write_text(langchain_snippets_content)

file_path.name
