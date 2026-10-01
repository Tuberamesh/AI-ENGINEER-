# DAY 27 — Prompt-Based Resume Analyzer

## Goal

Built a small AI application that compares a resume with a job description and produces a structured analysis.

## Input

```text
Resume + Job Description
```

## Output

```text
Matched Skills
Missing Skills
Experience Match
Suggestions
Score
```

## Application Flow

```text
Resume
   +
Job Description
   ↓
Context Preparation
   ↓
System Prompt + User Prompt
   ↓
LLM API
   ↓
Structured Output
   ↓
Pydantic Validation
   ↓
Final Result
```

## Prompt Roles

```text
System Prompt → Defines how the AI should behave
User Prompt   → Contains the actual task + resume + job description
```

## Project Structure

```text
resume-analyzer/
├── main.py
├── analyzer.py
├── .env
├── .gitignore
└── requirements.txt
```

## Pydantic Model

```python
class ResumeAnalysis(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    experience_match: str
    suggestions: list[str]
    score: int
```

This defines the expected output structure.

## Function Flow

```python
def analyze_resume(resume, job_description):
```

Receives:

```text
resume
job_description
```

Then:

```text
resume + job_description
        ↓
    user_prompt
        ↓
System Prompt + User Prompt
        ↓
      LLM
        ↓
ResumeAnalysis
```

## API Message Structure

```python
input=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]
```

Remember:

```text
role    → who is speaking
content → what they are saying
```

## Structured API Call

```python
response = client.responses.parse(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    text_format=ResumeAnalysis
)
```

`parse()` is useful here because the response is expected to follow the Pydantic structure.

```python
result = response.output_parsed
```

Returns the parsed `ResumeAnalysis` object.

## No API Key Version

Since no API key was available, the real LLM call was replaced with a mock:

```python
result = ResumeAnalysis(
    matched_skills=["Python", "SQL", "Pandas"],
    missing_skills=["AWS", "Docker"],
    experience_match="Good match for an entry-level role",
    suggestions=[
        "Add relevant AWS projects",
        "Highlight SQL projects"
    ],
    score=78
)
```

This allowed the complete application flow to be tested without calling an API.

## Key Revision

```text
Prompting
→ How to instruct the model

Context
→ Information given to the model

Structured Output
→ Predictable response format

Pydantic
→ Defines and validates that format

AI Application
→ Combines all of them into a working flow
```

## Day 27 Result

Built a prompt-based resume analyzer that demonstrates:

```text
Resume + JD
→ Context
→ Prompts
→ LLM
→ Structured Output
→ Validation
→ Final Analysis
```

## Main Lesson

A real AI application is not just a prompt.

```text
Prompt
+
Context
+
Model
+
Structured Output
+
Validation
=
Reliable AI Application Flow
```
