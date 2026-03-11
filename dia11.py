# Dia 11 - While: par/ímpar até digitar 0
X = 1
while X != 0:
    X = int(input('Digite um valor: '))
    if X % 2 == 0:
        print(f'{X} é Par')
    else:
        print(f'{X} é Impar')
print('Fim do programa')
