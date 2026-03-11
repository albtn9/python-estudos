# Dia 26 - PA com lista (quantidade definida)
P = int(input('Digite o primeiro numero: '))
R = int(input('Digite a Razão: '))
Q = int(input('Digite a Quantidade:'))
Termos = []
a = 0
while a < Q:
    Termos.append(P)
    print(P, end=',')
    P = P + R
    a += 1
print('\nLista resultante')
print(Termos)
print('\nFim do Programa')
