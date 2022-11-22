def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        candidate_l = candidate.lower()
        word_l = word.lower()
        if candidate_l == word_l:
            continue
        for char in candidate_l:
            if char not in word_l:
                break
            index = word_l.index(char)
            word_l = word_l[0:index] + word_l[index + 1:]
        else:
            if len(word_l) == 0:
                anagrams.append(candidate)
    return anagrams
