def add_or_increment(words, word):
    while word[-1] == "'":
        word = word[:-1]
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


def count_words(sentence):
    out = {}
    word = ""
    for char in sentence:
        if char.isalnum() or (char == "'" and len(word) > 0):
            word += char
        elif len(word) > 0:
            add_or_increment(out, word)
            word = ""
    if len(word) > 0:
        add_or_increment(out, word)
    return out
