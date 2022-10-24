stop = {"UAA", "UAG", "UGA"}

codon_map = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}


def proteins(strand):
    out = []
    for i in range(len(strand) // 3):
        codon = strand[i * 3: (i + 1) * 3]
        if codon in stop:
            break
        out.append(codon_map[codon])
    return out
