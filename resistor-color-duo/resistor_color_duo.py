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


def value(colors):
    d1 = numbers.index(colors[0])
    d2 = numbers.index(colors[1])
    return int(str(d1) + str(d2))
