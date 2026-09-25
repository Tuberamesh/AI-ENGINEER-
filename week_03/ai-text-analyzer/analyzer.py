from pydantic import BaseModel


class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str


def analyze_text(text):
    text = text.lower()

    # Sentiment
    if "love" in text or "enjoy" in text or "good" in text:
        sentiment = "positive"

    elif "hate" in text or "bad" in text or "worst" in text:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    # Keywords
    possible_keywords = [
        "product",
        "fast",
        "simple",
        "useful",
        "slow",
        "expensive",
        "cheap",
    ]

    keywords = []

    for word in possible_keywords:
        if word in text:
            keywords.append(word)

    # Category
    if "product" in text:
        category = "product review"

    elif "movie" in text:
        category = "movie review"

    elif "food" in text or "restaurant" in text:
        category = "food review"

    else:
        category = "general"

    result = {
        "summary": text,
        "sentiment": sentiment,
        "keywords": keywords,
        "category": category,
    }

    return AnalysisResult(**result)