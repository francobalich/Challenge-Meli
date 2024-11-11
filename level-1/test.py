from challenge import is_mutant

# Casos de prueba
test_cases = [
    ([
        "ATGCGA",
        "CAGTGC",
        "TTATTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG"
    ], False),  # Caso No Mutante

    ([
        "ATGCGA",
        "CAGTGC",
        "TTTTTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG"
    ], True),  # Caso Mutante con Secuencia Horizontal

    ([
        "ATGCGA",
        "AAGTGC",
        "ATATGC",
        "AGACGG",
        "ATGTCA",
        "TCACTG"
    ], True),  # Caso Mutante con Secuencia Vertical

    ([
        "ATGCGA",
        "CAGTAC",
        "TTATGT",
        "AGTAGG",
        "GCCTCA",
        "TCACTG"
    ], True),  # Caso Mutante con Secuencia Diagonal

    ([
        "AAAAGA",
        "CAGTGC",
        "TTATTT",
        "AGGGGG",
        "GCGTCA",
        "TCACTG"
    ], True),  # Caso Mutante con Secuencias en Diferentes Direcciones

    ([
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGACGG",
        "GCGTCA",
        "TCACTG"
    ], False)  # Caso No Mutante Sin Secuencias de 4 Iguales Consecutivas
]

# Ejecutar las pruebas
for i, (dna, expected) in enumerate(test_cases, 1):
    result = is_mutant(dna)
    print(f"Test {i}: {'Passed' if result == expected else 'Failed'} - Expected {expected}, got {result}")