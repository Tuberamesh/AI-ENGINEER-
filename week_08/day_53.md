# Day 53 — AI Agent Research Tools

**AI Engineering Journey | Week 08**

A practical implementation of standalone tools for AI agents, focusing on tool execution, database retrieval, document search, error handling, and execution boundaries.

## Overview

AI agents use external tools to retrieve information and perform actions. However, tools can fail, return incorrect results, or be used unnecessarily.

This project demonstrates how to build reliable Python tools that can later be integrated into an LLM-powered AI agent.

## Learning Objectives

- Understand limitations of AI agents.
- Understand hallucinations and incorrect tool selection.
- Prevent infinite loops and unnecessary tool calls.
- Handle tool execution failures.
- Implement input validation and error handling.
- Apply execution limits and basic safety boundaries.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| SQLite | Structured database storage |
| SQL | Database queries |
| pathlib | Local document handling |
| Logging | Execution monitoring |
| Python Exception Handling | Failure management |

No external API or paid service is required.

## Project Structure

```text
day53-agent-tools/
│
├── venv/
│
├── documents/
│   └── company.txt
│
├── main.py
├── company.db
└── README.md
```

## Tools Implemented

### 1. Calculator Tool

Performs basic mathematical operations.

Supported operations:
- Addition
- Subtraction
- Multiplication
- Division

Includes input validation and division-by-zero protection.

### 2. Database Search Tool

Uses SQLite to search structured customer and order information.

Database tables:
- customers
- orders

Features:
- SQL JOIN operations.
- Parameterized SQL queries.
- Search result limits.
- Database error handling.

### 3. Document Search Tool

Searches local `.txt` documents for relevant information.

Features:
- Keyword-based search.
- Case-insensitive matching.
- File size restrictions.
- Result limits.
- File error handling.

## Execution Control

A basic tool registry organizes the available tools:

```python
TOOLS = {
    "calculator": calculator,
    "database_search": database_search,
    "document_search": document_search
}
```

The execution controller provides:

- Unknown tool detection.
- Exception handling.
- Maximum tool-call limits.
- Duplicate action detection.

## Error Handling

The tools return consistent success and failure responses.

Successful execution:

```python
{
    "success": True,
    "result": "..."
}
```

Failed execution:

```python
{
    "success": False,
    "error": "Something went wrong"
}
```

This allows future agents to inspect tool results and decide what to do next.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd day53-agent-tools
```

Alternatively, open the existing project directory.

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Run the project

```bash
python main.py
```

The SQLite database is automatically initialized with sample customer and order records.

## Testing

The implementation includes tests for:

| Scenario | Expected behavior |
|---|---|
| Valid calculation | Returns result |
| Division by zero | Returns controlled error |
| Invalid operation | Rejects operation |
| Valid customer search | Returns matching records |
| Empty database query | Rejects input |
| Valid document search | Returns matching lines |
| Unknown tool | Rejects execution |
| Repeated tool calls | Blocks duplicate action |
| Exceeding call limit | Stops further execution |

## Key Engineering Concepts

- Tool registry
- Tool execution
- Database retrieval
- Document retrieval
- Parameterized SQL
- Input validation
- Exception handling
- Execution boundaries
- Duplicate action prevention

## Current Architecture

```text
          Python Application
                  |
                  v
              Tool Registry
                  |
        +---------+---------+
        |         |         |
        v         v         v
    Calculator  Database  Document
                Search     Search
        |         |         |
        +---------+---------+
                  |
                  v
            Tool Results
                  |
                  v
           Error Handling
                  |
                  v
           Execution Limits
```

## Current Limitations

- Tools are standalone and not yet connected to an LLM.
- Database search uses keyword matching.
- Document search supports plain text files only.
- No semantic search or vector database.
- No persistent agent conversation memory.
- Execution control is basic and requires further hardening.

## Future Improvements

1. Integrate tools with an LLM.
2. Implement dynamic tool selection.
3. Connect tools to the Day 52 agent loop.
4. Add conversation memory.
5. Implement retries and timeouts.
6. Add tool execution tracing.
7. Explore RAG and vector databases.

## Learning Outcome

Built three standalone Python tools with basic validation, error handling, and execution controls.

**Next milestone:** Integrate these tools into an LLM-powered AI agent with dynamic tool calling.

---

**Project:** Day 53 — Limitations & Research Tools  
**Track:** AI Engineering Journey  
**Week:** 08  
**Status:** Practical implementation
