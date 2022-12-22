import itertools


def combinations(target, size, exclude):
    out = set()
    for combination in itertools.combinations(set(range(1, 10)).difference(set(exclude)), size):
        if sum(combination) == target:
            out.add(combination)
    return sorted([list(i) for i in out])
