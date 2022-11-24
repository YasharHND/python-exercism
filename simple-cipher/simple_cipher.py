import string


class Cipher:
    def __init__(self, key=None):
        self.key = key if key is not None else "aaaaaaaaaa"

    def encode(self, text):
        out = ""
        for i, char in enumerate(text):
            convert_idx = string.ascii_lowercase.index(char) + string.ascii_lowercase.index(self.key[i % len(self.key)])
            if convert_idx > 25:
                convert_idx -= 26
            out += string.ascii_lowercase[convert_idx]
        return out

    def decode(self, text):
        out = ""
        for i, char in enumerate(text):
            convert_idx = string.ascii_lowercase.index(char) - string.ascii_lowercase.index(self.key[i % len(self.key)])
            out += string.ascii_lowercase[convert_idx]
        return out
