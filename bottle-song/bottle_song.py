numbers = (
    "No",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten"
)


def bottles(count):
    return "bottles" if count != 1 else "bottle"


def recite(start, take=1):
    out = []
    empty_line = False
    for i in reversed(range((start - take) + 1, start + 1)):
        if empty_line:
            out.append("")
        empty_line = True
        out.append(f"{numbers[i]} green {bottles(i)} hanging on the wall,")
        out.append(f"{numbers[i]} green {bottles(i)} hanging on the wall,")
        out.append(f"And if one green bottle should accidentally fall,")
        out.append(f"There'll be {numbers[i - 1].lower()} green {bottles(i - 1)} hanging on the wall.")
    return out
