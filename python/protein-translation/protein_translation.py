proteins_mapping = [
    ["Methionine", ["AUG"]],
    ["Phenylalanine", ["UUU", "UUC"]],
    ["Leucine", ["UUA", "UUG"]],
    ["Serine", ["UCU", "UCC", "UCA", "UCG"]],
    ["Tyrosine", ["UAU", "UAC"]],
    ["Cysteine", ["UGU", "UGC"]],
    ["Tryptophan", ["UGG"]],
    ["STOP", ["UAA", "UAG", "UGA"]],
]

def proteins(strand: str) -> list:
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    proteins = list()
    for codon in codons:
        for protein_mapping in proteins_mapping:
            for codon_mapping in protein_mapping[1]:
                if codon_mapping == codon:
                    if (protein_mapping[0] == "STOP"):
                        return proteins
                    proteins.append(protein_mapping[0])
    return proteins
