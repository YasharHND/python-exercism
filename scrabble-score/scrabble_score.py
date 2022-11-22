scores = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}


def find_score(char):
    char = char.upper()
    for value, characters in scores.items():
        if char in characters:
            return value


def score(word):
    final_score = 0
    for character in word:
        final_score += find_score(character)
    return final_score
