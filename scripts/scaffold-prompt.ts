#!/usr/bin/env tsx

import fs from "fs";
import path from "path";

const promptName = process.argv[2];

if (!promptName) {
  console.error(
    "❌ Please provide a prompt name.\nUsage: scaffold-prompt <prompt-name>"
  );
  process.exit(1);
}

const baseDir = path.join("prompts", promptName);
if (fs.existsSync(baseDir)) {
  console.error(`❌ Folder already exists: ${baseDir}`);
  process.exit(1);
}

// Create folder
fs.mkdirSync(baseDir, { recursive: true });

// Write placeholder prompt
fs.writeFileSync(
  path.join(baseDir, "prompt.txt"),
  `# ${promptName}\n\nYour prompt goes here.`
);

// Write placeholder test cases
fs.writeFileSync(
  path.join(baseDir, "test-cases.json"),
  JSON.stringify(
    [
      {
        input: "Example input",
        expected: "Expected output",
        options: {
          description: "Example test case"
        }
      }
    ],
    null,
    2
  )
);

// Write evalsuite config
fs.writeFileSync(
  path.join(baseDir, "evalsuite.yml"),
  `description: >
  Evaluation config for '${promptName}'.

prompts:
  - ./prompt.txt

tests:
  - ./test-cases.json

providers:
  - id: openai:gpt-4
    config:
      temperature: 0
      max_tokens: 512

metrics:
  - accuracy
  - cost
  - toxicity

plugins:
  - ../../evals/cost-checks.yml

output:
  format: markdown
  save: ./eval-report.md

options:
  show_diff: true
  hide_input: false

thresholds:
  minScore: 0.85
  minPassRate: 0.9
`
);

console.log(`✅ Scaffolded prompt folder: ${baseDir}`);
