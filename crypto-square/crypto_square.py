import math
import re


def cipher_text(plain_text):
    if plain_text == "":
        return ""
    normalized = re.sub("[^a-z1-9]+", "", plain_text.lower())
    sqrt_len = math.sqrt(len(normalized))
    rows = round(sqrt_len)
    if float(rows) != sqrt_len:
        normalized += "".join([" " for _ in range(rows - (len(normalized) % rows))])
    print(normalized)
    columns = len(normalized) // rows
    ciphered = []
    for i in range(columns):
        ciphered.append("".join([normalized[i + (j * columns)] for j in range(rows)]))
    return " ".join(ciphered)


out = cipher_text("Chill out.")
print(f">>>{out}<<<")
