def decode(string):
    if len(string) == 0:
        return ""
    result = ""
    count = "1"
    still_in_count = False
    for char in string:
        if char.isdigit():
            count = count + char if still_in_count else char
            still_in_count = True
        else:
            result += "".join([char for _ in range(int(count))])
            count = "1"
            still_in_count = False
    return result


def encode(string):
    if len(string) == 0:
        return ""
    result = ""
    last_char = string[0]
    count = 1
    for char in string[1:]:
        if char == last_char:
            count += 1
        else:
            result += f"{count}{last_char}" if count > 1 else last_char
            last_char = char
            count = 1
    result += f"{count}{last_char}" if count > 1 else last_char
    return result
