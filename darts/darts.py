import math


def score(x, y):
    d = math.sqrt(x ** 2 + y ** 2)
    return 10 if d <= 1 else 5 if d <= 5 else 1 if d <= 10 else 0

