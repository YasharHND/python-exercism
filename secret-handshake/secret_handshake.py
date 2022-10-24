def commands(binary_str):
    out = []
    if binary_str[-1] == "1":
        out.append("wink")
    if binary_str[-2] == "1":
        out.append("double blink")
    if binary_str[-3] == "1":
        out.append("close your eyes")
    if binary_str[-4] == "1":
        out.append("jump")
    if binary_str[-5] == "1":
        out.reverse()
    return out
