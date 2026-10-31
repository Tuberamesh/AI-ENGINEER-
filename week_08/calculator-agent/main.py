import ollama
from calculator import add, subtract, multiply, divide

tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtract",
            "description": "Subtract the second number from the first",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "divide",
            "description": "Divide the first number by the second",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

available_functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "What is 1500 multiplied by 25?"
        }
    ],
    tools=tools
)

for tool_call in response.message.tool_calls or []:
    function_name = tool_call.function.name
    arguments = tool_call.function.arguments

    result = available_functions[function_name](**arguments)

    print("Tool selected:", function_name)
    print("Tool result:", result)