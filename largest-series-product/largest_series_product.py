import functools


def largest_product(series, size):
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if size == 0:
        return 1
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if size < 0:
        raise ValueError("span must not be negative")
    out = 0
    for i in range((len(series) - size) + 1):
        product = functools.reduce(lambda x, y: x * y, map(int, [c for c in series[i:i + size]]))
        out = max(out, product)
    return out
