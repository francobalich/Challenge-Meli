import re

# Mutant case
#dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
# No mutant case
dna = ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]

def is_valid_dna(dna):
    """Valida que el ADN solo contenga caracteres A, T, G o C."""
    pattern = re.compile(r'^[ATGC]+$')
    return all(pattern.fullmatch(seq) for seq in dna)

def is_mutant(dna):
    if not dna:
        raise ValueError("DNA list cannot be empty")
    if not is_valid_dna(dna):
        raise ValueError("DNA contains invalid characters. Only A, T, G, and C are allowed.")

    n = len(dna)
    sequence_count = 0

    for row in dna:
        for i in range(n - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3]:
                sequence_count += 1
                if sequence_count > 1:
                    return True

    for col in range(n):
        for row in range(n - 3):
            if dna[row][col] == dna[row+1][col] == dna[row+2][col] == dna[row+3][col]:
                sequence_count += 1
                if sequence_count > 1:
                    return True

    for row in range(n - 3):
        for col in range(n - 3):
            if dna[row][col] == dna[row+1][col+1] == dna[row+2][col+2] == dna[row+3][col+3]:
                sequence_count += 1
                if sequence_count > 1:
                    return True
            if dna[row][col+3] == dna[row+1][col+2] == dna[row+2][col+1] == dna[row+3][col]:
                sequence_count += 1
                if sequence_count > 1:
                    return True
    return False
