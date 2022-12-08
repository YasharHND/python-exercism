numbers = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]


def label(colors):
    d1 = numbers.index(colors[0])
    d2 = numbers.index(colors[1])
    zero_count = numbers.index(colors[2])
    value = int(f"{d1}{d2}{'0' * zero_count}")
    kilo = value // 1000
    if kilo > 0:
        return f"{kilo} kiloohms"
    return f"{value} ohms"
