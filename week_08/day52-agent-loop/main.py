
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
