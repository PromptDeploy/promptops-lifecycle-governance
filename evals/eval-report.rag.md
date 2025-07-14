# 📊 PromptOps Eval Report: RAG Fallback Behavior

## Summary

| Model         | Tests Run | Passed | Failed | Pass Rate |
| ------------- | --------- | ------ | ------ | --------- |
| GPT-4o        | 2         | 2      | 0      | ✅ 100%   |
| Claude 3 Opus | 2         | 1      | 1      | ⚠️ 50%    |

---

## Detailed Results

### 🔹 GPT-4o

**Test:** RAG fallback: missing context  
✅ _Includes “don’t have enough information”_  
✅ _Did not include hallucinated content_

**Test:** RAG fallback: weak context  
✅ _Includes “weren’t found”_  
✅ _Did not include “reset password”_

---

### 🔸 Claude 3 Opus

**Test:** RAG fallback: missing context  
⚠️ _Response included speculative answer despite missing context_  
❌ _Failed includes check: “don’t have enough information” not found_  
✅ _No hallucinated terms detected_

**Test:** RAG fallback: weak context  
✅ _Includes “weren’t found”_  
✅ _Passed all assertions_

---

## Insights

- GPT-4o is more conservative with missing context and better avoids unsupported answers.
- Claude 3 may need additional grounding logic or stricter fallback instructions in prompt.

> 🧪 Consider extending test cases to include partial context, adversarial phrasing, or malicious prompt injection attempts.
