roman_numbers = (
    ("M", 1000, True),
    ("D", 500, False),
    ("C", 100, True),
    ("L", 50, False),
    ("X", 10, True),
    ("V", 5, False),
    ("I", 1, False),
)


def roman(number):
    out = ""
    remaining = number
    i = 0
    while remaining > 0:
        value = roman_numbers[i][1]
        symbol = roman_numbers[i][0]
        count = remaining // value
        one_tenth = value // 10
        if roman_numbers[i][2] and remaining // one_tenth == 9:
            out += roman_numbers[i + 2][0] + symbol
            remaining -= one_tenth * 9
            i += 1
        elif count == 4:
            out += symbol + roman_numbers[i - 1][0]
            remaining %= value
        else:
            out += symbol * count
            remaining %= value
            i += 1
    return out
