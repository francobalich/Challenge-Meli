import unittest
import sys
import os

# Agregar la ruta raíz del proyecto a `sys.path`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level_1.challenge import is_mutant  # Importación corregida

class TestIsMutant(unittest.TestCase):

    def test_mutant_case(self):
        dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        self.assertTrue(is_mutant(dna))

    def test_non_mutant_case(self):
        dna = ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
        self.assertFalse(is_mutant(dna))

    def test_invalid_characters(self):
        dna = ["ATGCGA", "CAGTXC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
        with self.assertRaises(ValueError):
            is_mutant(dna)

    def test_empty_dna(self):
        dna = []
        with self.assertRaises(ValueError):
            is_mutant(dna)

if __name__ == "__main__":
    unittest.main()
