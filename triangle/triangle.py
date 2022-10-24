def equity_test(sides):
    return (
        sum(sides) > 0 and
        sides[0] + sides[1] >= sides[2] and
        sides[0] + sides[2] >= sides[1] and
        sides[1] + sides[2] >= sides[0]
    )


def equilateral(sides):
    return (
        equity_test(sides) and
        sides[0] == sides[1] and
        sides[0] == sides[2] and
        sides[1] == sides[2]
    )


def isosceles(sides):
    return (
        equity_test(sides) and
        (sides[0] == sides[1] or
         sides[0] == sides[2] or
         sides[1] == sides[2])
    )


def scalene(sides):
    return (
        equity_test(sides) and
        sides[0] != sides[1] and
        sides[0] != sides[2] and
        sides[1] != sides[2]
    )
