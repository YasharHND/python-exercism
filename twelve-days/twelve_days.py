lines = (
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "a Partridge in a Pear Tree"
)

ordinals = (
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
)


def sing(length):
    day = "On the " + ordinals[length - 1] + " day of Christmas my true love gave to me: "
    verses = lines[-length:]
    if len(verses) > 1:
        verses = verses[:-1] + tuple(("and " + verses[-1],))
    joined = ", ".join(verses)
    return day + joined + "."


def recite(start_verse, end_verse):
    return [sing(n) for n in range(start_verse, end_verse + 1)]
