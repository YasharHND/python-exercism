def find_better(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
    index = len(search_list) // 2
    center_value = search_list[index]
    if center_value == value:
        return index
    if len(search_list) == 1:
        raise ValueError("value not in array")
    if value < center_value:
        result = find_better(search_list[:index], value)
        return index - result if result > 0 else 0
    if value > center_value:
        return index + find_better(search_list[index:], value)


def find(search_list, value):
    deviance = 0
    if len(search_list) % 2 == 0:
        search_list = [0 if value != 0 else 1] + search_list
        deviance = 1
    return find_better(search_list, value) - deviance
