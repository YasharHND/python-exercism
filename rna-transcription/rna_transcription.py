def to_rna_char(char):
    if char == "G":
        return "C"
    if char == "C":
        return "G"
    if char == "T":
        return "A"
    if char == "A":
        return "U"


def to_rna(dna_strand):
    if dna_strand == "":
        return ""
    return "".join([to_rna_char(char) for char in dna_strand])
