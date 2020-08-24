'''
Transcribe the given DNA strand into corresponding mRNA - a type of RNA,
that will be formed from it after transcription. DNA has the bases A, T, G and C,
while RNA converts to U, A, C and G respectively.
'''


def dna_to_rna(dna):
    return dna.translate(dna.maketrans('ATGC', 'UACG'))

# dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"
# dna_to_rna("CGATATA") ➞ "GCUAUAU"
# dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"

print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))
