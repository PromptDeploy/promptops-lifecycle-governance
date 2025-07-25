import fs from "fs";
import path from "path";

const PROMPTS_DIR = "prompts";
const REQUIRED_FILES = ["prompt.txt", "evalsuite.yml", "test-cases.json"];

let hasErrors = false;

function isValidName(name: string): boolean {
  return /^[a-z0-9\-]+$/.test(name);
}

function lintPromptFolder(folderPath: string, folderName: string) {
  console.log(`🔍 Linting ${folderName}...`);

  // Check naming
  if (!isValidName(folderName)) {
    console.error(
      `  ❌ Folder name "${folderName}" should be kebab-case (a-z, 0-9, -)`
    );
    hasErrors = true;
  }

  // Check required files
  for (const file of REQUIRED_FILES) {
    const filePath = path.join(folderPath, file);
    if (!fs.existsSync(filePath)) {
      console.error(`  ❌ Missing required file: ${file}`);
      hasErrors = true;
    }
  }
}

function main() {
  if (!fs.existsSync(PROMPTS_DIR)) {
    console.error(`❌ "${PROMPTS_DIR}" directory not found`);
    process.exit(1);
  }

  const folders = fs
    .readdirSync(PROMPTS_DIR)
    .filter((name) => fs.statSync(path.join(PROMPTS_DIR, name)).isDirectory());

  if (folders.length === 0) {
    console.warn(`⚠️  No prompt folders found in "${PROMPTS_DIR}"`);
    return;
  }

  for (const folderName of folders) {
    const folderPath = path.join(PROMPTS_DIR, folderName);
    lintPromptFolder(folderPath, folderName);
  }

  if (hasErrors) {
    console.error("\n❌ Lint failed. Please fix the issues above.\n");
    process.exit(1);
  } else {
    console.log("\n✅ All prompt folders passed lint checks.\n");
  }
}

main();
