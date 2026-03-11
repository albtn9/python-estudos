# Dia 1 - Soma de dois números

def somar(a: int, b: int) -> int:
    """Retorna a soma de a e b."""
    return a + b


if __name__ == "__main__":
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    r = somar(a, b)
    print("A soma de {} e {} resulta em {}".format(a, b, r))
