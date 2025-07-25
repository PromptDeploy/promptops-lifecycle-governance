import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const promptName = process.argv[2];

if (!promptName) {
  console.error(
    "❌ Please provide a prompt folder name.\nUsage: npm run test:prompt -- <prompt-folder>"
  );
  process.exit(1);
}

const configPath = path.join("prompts", promptName, "evalsuite.yml");

if (!fs.existsSync(configPath)) {
  console.error(`❌ Config not found at: ${configPath}`);
  process.exit(1);
}

try {
  console.log(`🧪 Evaluating prompt: ${promptName}`);
  execSync(`npx promptfoo eval --config ${configPath}`, { stdio: "inherit" });
} catch (err) {
  process.exit(1);
}
