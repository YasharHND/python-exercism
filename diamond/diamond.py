import string


def rows(letter):
    out = []
    limit = string.ascii_uppercase.index(letter)
    for row in range(-limit, limit + 1):
        indicator = limit - abs(row)
        line = ""
        for column in range(-limit, limit + 1):
            line += string.ascii_uppercase[indicator] if abs(column) == indicator else " "
        out.append(line)
    return out
