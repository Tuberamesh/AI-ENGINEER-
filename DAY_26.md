
# DAY 26 — Prompt Injection + Context Engineering

## What I Learned

### Prompt Injection

* Prompt injection = untrusted content contains instructions that try to influence the LLM.
* Direct injection = malicious instruction comes directly from the user.
* Indirect injection = malicious instruction is hidden inside external content such as PDFs, webpages, emails, or tool results.
* External content should be treated as **untrusted data**, not trusted instructions.

### Instructions vs Data

* **Instructions** = what the application tells the LLM to do.
* **Data** = information the LLM is asked to process.
* Important rule: instructions inside user-provided data should remain data, not become commands.
* Example: a resume saying "Ignore previous instructions" should be analyzed as resume content, not followed as an instruction.

### Basic Defenses

* Treat external content as untrusted.
* Clearly separate instructions from data.
* Explicitly tell the model not to follow instructions found inside untrusted content.
* Give the model only the tools/data it actually needs.
* Validate model outputs with schemas/Pydantic.
* Use least-privilege access for AI agents.

### Context Engineering

* **Prompt Engineering** = designing instructions for the LLM.
* **Context Engineering** = designing the information/environment given to the LLM.
* Context can include:

  * Instructions
  * User input
  * Examples
  * Documents
  * Conversation history
  * Retrieved information
  * Tool results
  * Structured data
* Context engineering focuses on **what information to include, what to exclude, and how to organize it**.

### Prompt Engineering vs Context Engineering vs AI Application Engineering

* Prompt Engineering → what should the model do?
* Context Engineering → what information should the model receive?
* AI Application Engineering → how do we build the complete reliable application around the model?

### Key Mental Model

* Instructions = commands.
* Data = information to process.
* Untrusted data can contain fake instructions.
* Context should contain relevant information, not everything available.
* Prompting → Context → LLM → Validation → Application.

## Day 26 Takeaway

**Prompt Engineering:** Design the instructions.
**Context Engineering:** Design the information around the instructions.
**AI Application Engineering:** Build the complete system that uses the LLM reliably and safely.
