"""
Testes unitários para dia1.py - Soma de dois números.
"""
import unittest
from dia1 import somar


class TestSomar(unittest.TestCase):
    """Testes da função somar."""

    def test_soma_positivos(self):
        """Soma de dois números positivos."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(10, 20), 30)

    def test_soma_negativos(self):
        """Soma de números negativos."""
        self.assertEqual(somar(-1, -1), -2)
        self.assertEqual(somar(-5, 3), -2)

    def test_soma_zero(self):
        """Soma com zero."""
        self.assertEqual(somar(0, 0), 0)
        self.assertEqual(somar(7, 0), 7)
        self.assertEqual(somar(0, 15), 15)

    def test_soma_grandes(self):
        """Soma de números maiores."""
        self.assertEqual(somar(100, 200), 300)
        self.assertEqual(somar(999, 1), 1000)


if __name__ == "__main__":
    unittest.main()
