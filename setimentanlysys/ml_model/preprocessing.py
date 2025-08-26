import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text
