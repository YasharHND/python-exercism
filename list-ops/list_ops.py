def append(list1, list2):
    return list1 + list2


def concat(lists):
    out = []
    for ls in lists:
        out.extend(ls)
    return out


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    acc = initial
    for i in list:
        acc = function(acc, i)
    return acc


def foldr(function, list, initial):
    if len(list) == 0:
        return initial
    acc = list[0]
    for i in list[1:]:
        acc = function(acc, i)
    return acc + initial


def reverse(list):
    out = []
    for i in list:
        out.insert(0, i)
    return out
