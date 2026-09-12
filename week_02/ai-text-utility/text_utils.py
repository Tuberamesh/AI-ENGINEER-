def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    return len(text)


def extract_keywords(text):
    words = text.lower().split()

    keywords = []

    for word in words:
        word = word.strip(".,!?;:")

        if len(word) > 4 and word not in keywords:
            keywords.append(word)

    return keywords[:5]

text = "Python is amazing for artificial intelligence development"

print("Words:", word_count(text))
print("Characters:", character_count(text))
print("Keywords:", extract_keywords(text))