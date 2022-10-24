def is_pangram(sentence):
    return all([chr(i) in sentence.upper() for i in range(65, 91)])
