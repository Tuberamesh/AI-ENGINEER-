# DAY 52 — Planning, Memory & Agent Loops

**Track:** AI Engineering Journey  
**Week:** 08 — AI Agents  
**Topics:** Planning, Memory, Agent Loops  
**Practical Project:** Basic Agent Loop with Memory

---

## 1. Learning Objectives

Today's goal is to understand how an AI agent:

- Plans and breaks down a task.
- Maintains conversation memory.
- Executes multiple actions.
- Decides its next action.
- Uses previous tool results.
- Knows when to stop executing.

**Deliverable:** A working Python agent loop with basic memory.

---

## 2. Planning in AI Agents

Planning means breaking a large user request into smaller, manageable actions.

Example:

**User request:**

"Research Python, identify three important AI engineering skills, and create a summary."

The agent can break this into:

1. Research Python for AI engineering.
2. Identify important AI engineering skills.
3. Organize the findings.
4. Generate a final summary.

### Important concepts

| Concept | Meaning |
|---|---|
| Planning | Decide what needs to be done |
| Action | Execute the selected operation |
| Observation | Understand the result of an action |
| Replanning | Decide the next step based on previous results |

An agent can modify its plan when a tool fails or returns unexpected information.

---

## 3. Memory in AI Agents

Memory allows an agent to use information from previous interactions and actions.

### Types of memory

**1. Short-term memory**

Stores current conversation context.

Example: Previous user messages.

**2. Working memory**

Stores intermediate information required to complete the current task.

Example: Tool results, completed steps and current progress.

**3. Long-term memory**

Stores information that can be reused across different sessions.

Example: User preferences and project information.

### Basic Python memory

```python
memory = {
    "conversation": [],
    "tool_results": [],
    "completed_steps": []
}
```

Memory is useful because the agent can refer to previous information instead of starting from zero after every action.

---

## 4. Agent Loops

An agent loop is a repeated process in which an agent decides, executes and observes until the task is complete.

### Basic execution cycle

1. Think.
2. Decide.
3. Act.
4. Observe.
5. Repeat or stop.

### Pseudocode

```python
while True:

    decision = agent_decides()

    if decision == "STOP":
        break

    result = execute_tool(decision)

    memory.append(result)
```

### Why do agents need loops?

An agent may need multiple actions to complete a single task.

For example:

- Search for information.
- Read the search results.
- Calculate relevant values.
- Generate a summary.

The result of one action becomes context for the next decision.

---

## 5. How Agents Decide Their Next Action

An agent evaluates the current task, available tools and previous observations.

Example:

**User:** Find the average of 10, 20 and 30.

Available tools:

- Calculator
- Search

The agent identifies that this is a mathematical task and selects the calculator.

Execution:

```text
User request
    |
    v
Agent decision
    |
    v
Select calculator
    |
    v
Execute calculation
    |
    v
Observe result: 20
    |
    v
Check whether task is complete
    |
    v
Generate final answer
```

This is observation-based decision-making.

---

## 6. Practical Implementation

### Project structure

```text
week_08/
│
├── day52-agent-loop/
│   │
│   ├── venv/
│   └── main.py
│
└── day 52.md
```

### Step 1: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Step 2: Implement the agent

File: `main.py`

```python
# DAY 52: Basic Agent Loop

# 1. Agent memory
memory = {
    "conversation": [],
    "tool_results": [],
    "completed_steps": []
}


# 2. Available tools
def calculator(expression):

    allowed = {
        "add": lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "average": lambda a, b, c: (a + b + c) / 3
    }

    operation = expression["operation"]
    numbers = expression["numbers"]

    return allowed[operation](*numbers)


def create_summary(results):

    return f"Task completed. Results: {results}"


# 3. Agent decision function
def agent_decides(task, memory):

    completed = memory["completed_steps"]

    if "calculate" not in completed:

        return {
            "action": "calculator",
            "input": {
                "operation": "average",
                "numbers": [10, 20, 30]
            }
        }

    if "summarize" not in completed:

        return {
            "action": "summarize",
            "input": memory["tool_results"]
        }

    return {"action": "stop"}


# 4. Tool execution
def execute_tool(decision):

    action = decision["action"]
    data = decision.get("input")

    if action == "calculator":
        return calculator(data)

    if action == "summarize":
        return create_summary(data)

    return None


# 5. Agent loop
def run_agent(task):

    print("\nAgent started:", task)

    memory["conversation"].append({
        "role": "user",
        "content": task
    })

    max_steps = 5

    for step in range(max_steps):

        print(f"\n--- Agent Step {step + 1} ---")

        # Decide next action
        decision = agent_decides(task, memory)

        print("Decision:", decision)

        # Stop condition
        if decision["action"] == "stop":

            print("\nAgent decided to stop.")
            break

        # Execute action
        result = execute_tool(decision)

        print("Tool result:", result)

        # Store result in memory
        memory["tool_results"].append(result)

        memory["completed_steps"].append(
            "calculate" if decision["action"] == "calculator"
            else "summarize"
        )

    memory["conversation"].append({
        "role": "assistant",
        "content": memory["tool_results"][-1]
    })

    print("\nFinal answer:")
    print(memory["tool_results"][-1])


# 6. Run agent
if __name__ == "__main__":

    user_task = "Calculate the average of 10, 20 and 30."

    run_agent(user_task)
```

### Step 3: Execute

```bash
python main.py
```

### Expected output

```text
Agent started: Calculate the average of 10, 20 and 30.

--- Agent Step 1 ---
Decision: calculator
Tool result: 20.0

--- Agent Step 2 ---
Decision: summarize
Tool result: Task completed. Results: [20.0]

--- Agent Step 3 ---
Decision: stop

Agent decided to stop.

Final answer:
Task completed. Results: [20.0]
```

---

## 7. Understanding the Execution

| Step | What happened? |
|---|---|
| Step 1 | Agent selected the calculator |
| Step 2 | Calculator returned 20.0 |
| Step 3 | Agent selected the summarizer |
| Step 4 | Summary was generated |
| Step 5 | Agent recognized that all steps were complete and stopped |

**Important:** This implementation uses a rule-based decision function, not an LLM. It demonstrates the underlying agent-loop architecture.

In an actual AI agent, an LLM can dynamically select tools and actions based on the user request, available tools and previous observations.

---

## 8. When Should an Agent Stop?

An agent should stop when:

1. The requested task is completed.
2. Sufficient information is available.
3. Required information is missing.
4. A tool repeatedly fails.
5. The maximum iteration limit is reached.

### Maximum iteration protection

```python
MAX_STEPS = 10

for step in range(MAX_STEPS):

    # Agent decision and execution
    pass
else:
    print("Maximum steps reached.")
```

This prevents infinite loops, unnecessary API calls and excessive token usage.

---

## 9. Important Engineering Concepts

| Concept | Purpose |
|---|---|
| Task decomposition | Break complex tasks into smaller steps |
| Working memory | Retain intermediate results |
| Tool calling | Allow agents to execute external functions |
| Observation | Read and understand tool results |
| Replanning | Adapt the next action |
| Stop condition | Determine when execution should end |
| Max iterations | Prevent uncontrolled execution |

---

## 10. Key Takeaways

- Planning helps agents break complex tasks into smaller actions.
- Memory provides access to previous interactions and results.
- Agent loops allow multiple actions to happen sequentially.
- Tool results influence the next agent decision.
- Stop conditions prevent unnecessary execution.
- Maximum iteration limits protect production systems.

**Most important concept:**

An AI agent is not simply an LLM that generates text. It is a system that combines an LLM, tools, memory, decision-making and an execution loop.

---

## 11. Future Learning

Next topic: ** — Limitations & Research Tools**

Topics:

- Limitations of AI agents.
- Hallucinations and incorrect tool usage.
- Infinite loops and execution failures.
- Research tools and web search.
- Reliability and validation.
- Human approval and control.