# DAY 51 — Tool Calling & Function Calling

## Concepts
1. Tool calling
2. Function calling
3. Tool calling vs function calling
4. Tool selection
5. Tool arguments
6. Tool execution
7. Tool results
8. LLM response after tool execution

## Practical Implementation

Project: AI Calculator Agent

Technologies:
- Python
- Ollama
- Qwen3 1.7B
- Ollama Python SDK

## Functions Implemented
- add()
- subtract()
- multiply()
- divide()

## Architecture

User
  |
  v
LLM
  |
Tool Request
  |
Python Function
  |
Tool Result
  |
LLM
  |
Final Answer

## Important Learnings
- LLM selects tools based on user intent.
- Tool arguments contain the required inputs.
- Python executes the actual function.
- Tool results are returned to the LLM.
- LLM generates the final response.
- Tool execution must be controlled by the application.

## DAY 51 COMPLETED


## Practical Project: Calculator Agent

- Model: qwen2.5:3b
- Runtime: Ollama
- Language: Python
- SDK: ollama

### Tools implemented
- add()
- subtract()
- multiply()
- divide()

### Successful test
Question: What is 1500 multiplied by 25?

LLM-selected tool: multiply
Arguments: 1500, 25
Python result: 37500

### Key Learning
The LLM decides which tool to call.
Python executes the tool.
The tool result is returned to the application.