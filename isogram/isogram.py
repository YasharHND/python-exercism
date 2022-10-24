import re


def is_isogram(string):
    cleaned = re.sub(r'[ -]+', '', string)
    chars = set()
    for char in cleaned.lower():
        chars.add(char)
    return len(chars) == len(cleaned)
