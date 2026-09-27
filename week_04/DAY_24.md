
# DAY 24 — Better Prompting

## What I Learned

### 1. Examples in Prompts
Examples show the LLM the pattern we want.

Example:
Input: Python
Output: Programming Language

Input: PostgreSQL
Output: Database

Input: Docker
Output: Tool

### 2. Zero-Shot Prompting
No examples are given.

Instruction → Input → Output

### 3. Few-Shot Prompting
A few examples are given before the new input.

Instruction → Examples → New Input → Output

Use few-shot when the task, categories, or output format needs clarification.

### 4. When Examples Help
Examples help with:
- Custom classification
- Ambiguous tasks
- Specific output formats
- Consistent responses
- Showing the expected pattern

Start with zero-shot → test → add examples only if needed.

### 5. Prompt Templates
A reusable prompt with changing variables.

Example:

Classify this skill.

Skill: {skill}

Output only the category.

The {skill} value can change without rewriting the whole prompt.

### 6. Clear Input & Output
Clearly define:
- What the model should do
- What the input is
- What the output should look like

Bad:
Tell me about Python.

Better:
Classify Python as Programming Language, Database, or Tool.
Output only the category.

### 7. Classification
Input → Category

Example:
Python → Programming Language
PostgreSQL → Database

### 8. Extraction
Text → Specific information

Example:
"I bought a MacBook for ₹85,000 from Amazon."

Product → MacBook
Price → ₹85,000
Store → Amazon

### 9. Structured Output
Ask the LLM for a predictable format such as JSON.

Example:

{
  "product": "MacBook",
  "price": "₹85,000",
  "store": "Amazon"
}

If information is missing:

Missing field → null

### 10. Good vs Bad Prompts

Bad:
Classify this.

Good:
Classify the following skill into exactly one category.

Categories:
- Programming Language
- Database
- Tool
- Framework
- Library

Input:
{skill}

Output only the category.

### Practical Prompt Structure

Task
↓
Rules / Constraints
↓
Examples (optional)
↓
Input
↓
Output Format

### Quick Revision

Zero-shot → No examples
Few-shot → Examples included
Prompt Template → Reusable prompt + variable
Classification → Input → Category
Extraction → Text → Information
Structured Output → Predictable format
Good Prompt → Clear task + input + constraints + output

## Key Takeaway

Good prompting is not about making prompts long.

It is about making the task, input, constraints, examples, and expected output clear.
```
