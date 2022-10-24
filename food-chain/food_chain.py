verses = [
    ("fly", None),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!")
]


def recite(start_verse, end_verse):
    out = []
    separate_verses = False
    for i in range(start_verse, end_verse + 1):
        if separate_verses:
            out.append("")
        out += recite_verse(i)
        separate_verses = True
    return out


def recite_verse(verse_number):
    out = []
    item = verses[verse_number - 1]
    animal = item[0]
    complementary_sentence = item[1]
    out.append("I know an old lady who swallowed a " + animal + ".")
    if animal is "horse":
        out.append(complementary_sentence)
        return out
    if animal is not "fly":
        out.append(complementary_sentence)
        for i in reversed(range(1, verse_number)):
            eater = verses[i][0]
            eaten = verses[i - 1][0]
            swallow_sentence = "She swallowed the " + eater + " to catch the " + eaten
            swallow_sentence += "." if eaten != "spider" else " that wriggled and jiggled and tickled inside her."
            out.append(swallow_sentence)
    out.append("I don't know why she swallowed the fly. Perhaps she'll die.")
    return out
