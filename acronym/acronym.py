import re


def abbreviate(words):
    return "".join([word[0].upper() for word in re.sub("[ _-]+", " ", words).split()])
