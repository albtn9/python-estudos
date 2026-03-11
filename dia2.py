# Dia 2 - Divisão (com verificação de zero)
import sys
import unittest


def dividir(a: int, b: int):
    """
    Retorna a divisão de a por b.
    Levanta ValueError se A ou B forem zero.
    """
    if a == 0 or b == 0:
        raise ValueError("Não é possivel calcular a divisão")
    return a / b


class TestDividir(unittest.TestCase):
    """Testes da função dividir (dentro do próprio dia2.py)."""

    def test_divisao_normal(self):
        """Divisão entre números válidos."""
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(9, 3), 3.0)

    def test_divisao_retorna_float(self):
        """Resultado é float mesmo com divisão exata."""
        self.assertEqual(dividir(7, 2), 3.5)

    def test_divisor_zero_levanta_erro(self):
        """Divisor zero deve levantar ValueError."""
        with self.assertRaises(ValueError) as ctx:
            dividir(5, 0)
        self.assertIn("Não é possivel calcular", str(ctx.exception))

    def test_dividendo_zero_levanta_erro(self):
        """Dividendo zero deve levantar ValueError."""
        with self.assertRaises(ValueError):
            dividir(0, 10)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        unittest.main(argv=sys.argv[:1] + sys.argv[2:])
    else:
        A = int(input('Digite o valor de A: '))
        B = int(input('Digite o valor de B: '))
        if A == 0 or B == 0:
            print('Não é possivel calcular a divisão')
        else:
            R = dividir(A, B)
            print('A Divisão é :', R)
