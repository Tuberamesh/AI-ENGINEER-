import json

from analyzer import analyze_text


text = input("Enter your text: ")

result = analyze_text(text)

with open("result.json", "w") as file:
    json.dump(result.model_dump(), file, indent=4)

print("Analysis saved to result.json")