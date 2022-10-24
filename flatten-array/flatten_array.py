def flatten(iterable, main=None):
    if main is None:
        main = []
    if isinstance(iterable, int):
        main.append(iterable)
    elif isinstance(iterable, list):
        for i in iterable:
            flatten(i, main)
    return main
