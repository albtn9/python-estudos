# Dia 13 - Progressão Aritmética (10 termos)
P = int(input('Digite o primeiro numero: '))
R = int(input('Digite a Razão: '))
cont = 1
while cont <= 10:
    print(P, end=' - ')
    P = P + R
    cont += 1
