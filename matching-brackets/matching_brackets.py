opening = {"(", "{", "["}
closing = {")", "}", "]"}


def is_paired(input_string):
    mapped = []
    for char in input_string:
        if char in opening:
            mapped.append(char)
        elif char in closing:
            if len(mapped) == 0:
                return False
            if char == ")":
                if mapped.pop() != "(":
                    return False
            elif char == "}":
                if mapped.pop() != "{":
                    return False
            else:
                if mapped.pop() != "[":
                    return False
    return len(mapped) == 0
