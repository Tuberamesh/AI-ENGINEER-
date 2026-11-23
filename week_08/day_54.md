# 🤖 AI Research Assistant

**An LLM-powered AI agent that researches information, executes Python tools, searches databases, retrieves documents, and handles multi-step tasks.**

Built with Python, Ollama, and Qwen 2.5 3B.

---

## 🧠 Project Overview

The AI Research Assistant uses an LLM as its reasoning engine. Instead of simply generating text, it can select and execute external tools based on the user's question.

It supports:

- Mathematical calculations
- Customer and order database searches
- Local document searches
- Automatic tool selection
- Multi-step agent execution
- Basic conversation memory
- Tool validation and error handling

## 🏗️ System Architecture

```text
                       USER
                         |
                         v
                +------------------+
                |  User Question   |
                +------------------+
                         |
                         v
              +----------------------+
              |    LLM - Qwen 2.5    |
              |    (Ollama Local)    |
              +----------------------+
                         |
                         v
              +----------------------+
              |   Tool Selection     |
              | Understand the task  |
              +----------------------+
                         |
                         v
              +----------------------+
              |    Agent Loop        |
              |                      |
              |  1. Decide           |
              |  2. Execute          |
              |  3. Observe          |
              |  4. Repeat / Stop    |
              +----------------------+
                         |
                         v
                +----------------+
                |  Tool Registry |
                +----------------+
                   /     |      \
                  /      |       \
                 v       v        v
          +----------+ +--------+ +----------+
          |Calculator| |Database| |Documents |
          |          | | Search | |  Search  |
          +----------+ +--------+ +----------+
               |          |          |
               v          v          v
          +----------+ +--------+ +----------+
          | Arithmetic| | SQLite | | Text     |
          | Results   | | Records| | Files    |
          +----------+ +--------+ +----------+
                 \       |       /
                  \      |      /
                   v     v     v
              +----------------------+
              |   Tool Observations  |
              |   Basic Memory       |
              +----------------------+
                         |
                         v
              +----------------------+
              |   LLM Final Answer   |
              +----------------------+
                         |
                         v
                        USER
```

## 🔄 Agent Execution Flow

```text
User asks a question
        |
        v
LLM understands the request
        |
        v
Does the task require a tool?
        |
    +---+---+
    |       |
   YES      NO
    |       |
    v       v
Select     Generate
tool       response
    |
    v
Python validates