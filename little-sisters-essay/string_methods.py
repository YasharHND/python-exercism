def capitalize_title(title):
    return " ".join([w.capitalize() for w in title.split(" ")])


def check_sentence_ending(sentence):
    return sentence[len(sentence) - 1] in {".", "?", "!"}


def clean_up_spacing(sentence):
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)
