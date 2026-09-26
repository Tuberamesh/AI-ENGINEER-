# DAY 23 — Prompt Fundamentals

## 🎯 Goal

Understand how to give an LLM clear instructions instead of simply asking random questions.

## 1. What is a Prompt?

A prompt is the input we give to an LLM to tell it what we want it to do.

Example:

```
Explain Python lists.
```

A prompt can be a question, instruction, context, constraints, or a combination of these.

The main idea:

> A prompt guides the LLM toward the desired output.

## 2. System Prompt

A system prompt gives the LLM high-level behavior, role, or rules.

Example:

```
SYSTEM:
You are a professional resume analyzer.
```

Think:

> System = How should the AI behave?

## 3. User Prompt

A user prompt contains the user's specific request or input.

Example:

```
USER:
Analyze this resume against the job description.
```

Think:

> User = What does the user want the AI to do?

## 4. System vs User

Simple mental model:

```
SYSTEM → How should you behave?
USER   → What should you do?
```

Example:

```
SYSTEM:
You are a SQL tutor.
Explain concepts simply.

USER:
Explain INNER JOIN with an example.
```

The system establishes general behavior, while the user provides the specific task.

## 5. Instructions

An instruction tells the LLM what action it should perform.

Examples:

```
Summarize this article.
Extract the customer's name.
Classify this review.
Analyze this resume.
Compare these two products.
```

Think:

> Instruction = What should the LLM do?

## 6. Context / Input

Context is the information the LLM should work with.

Example:

```
Instruction:
Analyze this review.

Context:
"The product is fast and easy to use."
```

So:

```
Instruction → What should the LLM do?
Context     → What should the LLM work on?
```

## 7. Constraints

A constraint limits what the LLM can do or how it should respond.

Example:

```
CONSTRAINTS:
- Use only the provided information.
- Do not invent skills.
- Keep the answer under 100 words.
```

Think:

```
Instruction → What to do
Constraint  → Limits on how to do it
```

## 8. Why Constraints Matter

LLMs are flexible. Without constraints, they may produce unnecessary details, assumptions, long responses, or unwanted formatting.

Constraints make the output more predictable.

Example:

```
Analyze this resume.

Constraints:
- Use only provided information.
- Do not invent skills.
- Keep the response concise.
```

This becomes especially useful when building AI applications where the output needs to follow specific rules.

## 9. Instruction Priority

When multiple instructions exist, they can have different priorities.

A simplified model is:

```
SYSTEM
   ↓
DEVELOPER
   ↓
USER
```

Higher-priority instructions generally take precedence over lower-priority instructions when they conflict.

Example:

```
SYSTEM:
Always respond in JSON.

USER:
Write the answer as a normal paragraph.
```

The higher-priority instruction should take precedence.

Important AI Engineering point:

> Instruction priority is not the same as application security.

A prompt saying "Never reveal confidential information" does not automatically make an application secure.

Real applications may still require authentication, authorization, access control, input validation, output validation, and proper data protection.

## 10. Basic Prompt Structure

A practical prompt can contain:

```
SYSTEM:
Role / behavior

USER:
Instruction

Context / Input

Constraints

Output format
```

Example:

```
SYSTEM:
You are a professional resume analyzer.

USER:
Analyze the resume against the job description.

RESUME:
[resume text]

JOB DESCRIPTION:
[job description]

CONSTRAINTS:
- Use only the provided information.
- Do not invent skills.
- Keep the response concise.

OUTPUT:
Return:
1. Matching skills
2. Missing skills
3. Relevant experience
```

This is much clearer than simply saying:

```
Tell me about this resume.
```

## 🧠 Complete Mental Model

```
PROMPT
   │
   ├── SYSTEM → Behavior / rules
   │
   ├── USER → Task / input
   │
   ├── INSTRUCTION → What should the model do?
   │
   ├── CONTEXT → What information should it use?
   │
   ├── CONSTRAINTS → What limits must it follow?
   │
   └── OUTPUT FORMAT → How should the result look?
              │
              ↓
             LLM
              │
              ↓
           RESPONSE
```

## 🔑 Key Takeaway

Prompting is not just asking questions.

It is about designing a clear task for the LLM.

Instead of:

```
Analyze this resume.
```

We can provide:

```
SYSTEM:
You are a professional resume analyzer.

USER:
Analyze this resume against the job description.

CONSTRAINTS:
- Use only provided information.
- Do not invent skills.
- Keep the response concise.

OUTPUT:
- Matching skills
- Missing skills
- Relevant experience
```

The goal is to make the LLM's task clear, controlled, and predictable.

## ✅ DAY 23 COMPLETE

Topics covered:

* [x] What is a prompt?
* [x] System prompt
* [x] User prompt
* [x] System vs User instructions
* [x] Instructions
* [x] Context / Input
* [x] Constraints
* [x] Why constraints matter
* [x] Instruction priority
* [x] Basic prompt structure

> DAY 23 COMPLETE — Prompt Fundamentals
