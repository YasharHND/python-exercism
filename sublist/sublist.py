SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def is_sublist(list_one, list_two):
    l1 = len(list_one)
    l2 = len(list_two)
    for i in range((l2 - l1) + 1):
        if list_two[i:i + l1] == list_one:
            return True
    return False


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] != list_two[i]:
                return UNEQUAL
        return EQUAL
    if len(list_one) > len(list_two):
        return SUPERLIST if is_sublist(list_two, list_one) else UNEQUAL
    if len(list_two) > len(list_one):
        return SUBLIST if is_sublist(list_one, list_two) else UNEQUAL
    else:
        return UNEQUAL
