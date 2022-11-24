def bottle(count):
    if count > 1:
        return f"{count} bottles"
    if count == 1:
        return "1 bottle"
    return "No more bottles"


def recite(start, take=1):
    out = []
    empty_line = False
    start += 1
    for i in reversed(range(start - take, start)):
        bottles = bottle(i)
        if empty_line:
            out.append("")
        out.append(f"{bottles} of beer on the wall, {bottles.lower()} of beer.")
        if i > 0:
            out.append(f"Take {'one' if i > 1 else 'it'} down and pass it around, {bottle(i - 1).lower()} of beer on the wall.")
        else:
            out.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        empty_line = True
    return out
