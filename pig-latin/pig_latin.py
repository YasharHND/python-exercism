vowels = {"a", "e", "i", "o", "u"}
like_vowels = {"xr", "yt"}
consonant_clusters = {"ch", "th", "qu", "rh"}
consonant_clusters_3 = {"sch", "thr"}


def translate(text):
    return " ".join(map(translate_one, text.split()))


def translate_one(text):
    if text[0] in vowels or text[0:2] in like_vowels:
        return text + "ay"
    if text[0:3] in consonant_clusters_3:
        return text[3:] + text[0:3] + "ay"
    if text[0:2] in consonant_clusters:
        return text[2:] + text[0:2] + "ay"
    if text[1:3] == "qu":
        return text[3:] + text[0:3] + "ay"
    if text[0] not in vowels:
        return text[1:] + text[0] + "ay"
