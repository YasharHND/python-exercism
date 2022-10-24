to_ignore = "., "
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba1234567890"


def encode(plain_text):
    parts = []
    part = ""
    for char in plain_text.lower():
        if char in to_ignore:
            continue
        part += reversed_alphabet[alphabet.index(char)]
        if len(part) % 5 == 0:
            parts.append(part)
            part = ""
    if len(part):
        parts.append(part)
    return " ".join(parts)


def decode(ciphered_text):
    return "".join([alphabet[reversed_alphabet.index(char)] if char != " " else "" for char in ciphered_text])


print(decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"))
