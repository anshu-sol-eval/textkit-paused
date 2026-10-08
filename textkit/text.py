import re


def truncate(text, limit, suffix="..."):
    """Shorten text to at most `limit` characters, including the suffix."""
    if len(text) <= limit:
        return text
    return text[:limit] + suffix


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def word_count(text):
    return len(text.split(" "))
