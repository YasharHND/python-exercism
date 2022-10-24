def rotate_char(char, key):
    upper = char.isupper()
    target = ord(char.lower()) + key
    if target > 122:
        target = 96 + (target - 122)
    out = chr(target)
    return out.upper() if upper else out


def rotate(text, key):
    return ''.join([rotate_char(c, key) if c.isalpha() else c for c in text])
