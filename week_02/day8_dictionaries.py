# data = {
#     "name": "Ramesh",
#     "skills": ["Python", "SQL"],
#     "experience": 0
# }

# print(data["name"])
# print(data["skills"])
# print(data["experience"])
# data["college"] = "NHCE"
# data["experience"] = 1
# print(data["college"])
# print(data["experience"])

import json
text = """
Python is a powerful programming language.
Python is widely used in data science and AI.
I am learning Python for AI engineering.
"""

# words = text.split()
# word_count = len(words)
# print(word_count)
# character_count = len(text)
# print(character_count)

# result = {
#     "text": text,
#     "word_count": word_count,
#     "character_count": character_count
# }

# print(result)

# with open("result.json", "w") as file:
#     json.dump(result, file, indent=4)

# with open("result.json", "r") as file:
#     data = json.load(file)
#     print(data)


# with open("sample.txt", "w") as file:
#     file.write("Hello, I am learning Python.")

# with open("sample.txt", "a") as file:
#     file.write("\nThis is another line.")

# with open("sample.txt", "r") as file:
#     content = file.read()

# print(content)

students = [
    {"name": "Ramesh", "branch": "Data Science"},
    {"name": "Rahul", "branch": "CSE"},
    {"name": "Anu", "branch": "ISE"}
]

for student in students:
    print(student["name"], "-", student["branch"])