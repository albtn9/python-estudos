# Dia 14 - Múltiplos de D (até 100)
D = int(input('Digite o Valor:'))
if D <= 0:
    print('Fim do Programa')
else:
    i = 1
    while i < 100:
        if i % D == 0:
            print(i, end='  ')
        i += 1
    print('\n\nFim do Programa')
