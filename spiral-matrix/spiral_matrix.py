directions = {
    "R": {
        "next": "D",
        "axis": "x",
        "changer": +1
    },
    "D": {
        "next": "L",
        "axis": "y",
        "changer": +1
    },
    "L": {
        "next": "U",
        "axis": "x",
        "changer": -1
    },
    "U": {
        "next": "R",
        "axis": "y",
        "changer": -1
    }}


def spiral_matrix(size):
    output = [[0 for _ in range(size)] for _ in range(size)]
    directions["R"]["threshold"] = size - 1
    directions["D"]["threshold"] = size - 1
    directions["L"]["threshold"] = 0
    directions["U"]["threshold"] = 1
    cd = directions["R"]
    x = 0
    y = 0
    for i in range(size ** 2):
        output[y][x] = i + 1
        if cd["axis"] == "x":
            if x == cd["threshold"]:
                cd["threshold"] -= cd["changer"]
                cd = directions[cd["next"]]
                y += cd["changer"]
            else:
                x += cd["changer"]
        elif cd["axis"] == "y":
            if y == cd["threshold"]:
                cd["threshold"] -= cd["changer"]
                cd = directions[cd["next"]]
                x += cd["changer"]
            else:
                y += cd["changer"]
    return output
