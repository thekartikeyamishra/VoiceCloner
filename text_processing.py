import re


def clean_text(text, language="en"):
    text = text.strip()
    if language == "en":
        text = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)
    elif language == "hi":
        text = re.sub(r"[^\u0900-\u097F\s.,!?']" " ", text)  # For Hindi
    return text.lower()
