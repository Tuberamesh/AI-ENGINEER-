import json

from text_utils import word_count, character_count, extract_keywords
from api_utils import get_api_data


text = "Python is amazing for building AI applications."

words = word_count(text)
characters = character_count(text)
keywords = extract_keywords(text)

api_data = get_api_data()


result = {
    "text": text,
    "word_count": words,
    "character_count": characters,
    "keywords": keywords,
    "api_data": api_data
}


with open("result.json", "w") as file:
    json.dump(result, file, indent=4)


print("\n--- Text Analysis ---")
print("Words:", words)
print("Characters:", characters)
print("Keywords:", keywords)
print("API Data:", api_data)