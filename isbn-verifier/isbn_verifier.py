import re


def numberize(char):
    return 10 if char == 'X' else int(char) if char.isnumeric() else 11


def is_valid(isbn):
    cleaned = re.sub('-', '', isbn)
    if len(cleaned) != 10:
        return False
    digits = []
    for i in range(10):
        d = numberize(cleaned[i])
        if d > 10 or (d == 10 and i != 9):
            return False
        digits.append(d)
    return sum([digits[i] * (10 - i) for i in range(10)]) % 11 == 0
