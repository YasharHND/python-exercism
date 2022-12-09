def proverb(*args, qualifier):
    if not args:
        return []
    out = []
    for i in range(len(args) - 1):
        out.append(f"For want of a {args[i]} the {args[i + 1]} was lost.")
    out.append(f"And all for the want of a {qualifier + ' ' if qualifier else ''}{args[0]}.")
    return out
