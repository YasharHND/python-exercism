def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    base_10 = 0
    for i in range(len(digits)):
        d = digits[-1 - i]
        if d >= input_base or d < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        base_10 += d * (input_base ** i)
    p = 2
    while output_base ** p < base_10:
        p += 1
    p -= 1
    r = base_10
    if base_10 == 0:
        return [0]
    out = []
    for i in reversed(range(p + 1)):
        m = output_base ** i
        d = r // m
        r %= m
        if d == 0 and i == p:
            continue
        out.append(d)
    return out
