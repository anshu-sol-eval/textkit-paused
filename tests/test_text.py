from textkit import slugify, truncate


def test_short_text_unchanged():
    assert truncate("hi", 10) == "hi"


def test_slugify():
    assert slugify("  Hello, World! ") == "hello-world"
