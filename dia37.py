# Dia 37 - Celsius para Fahrenheit e sensação
C = float(input('Quantos Graus ta no Brasil : '))
F = 9*C/5 + 32
if F < 45:
    print('Até que ta frio')
elif F < 75:
    print('Até que ta bom')
else:
    print('Ai tá quente')
print(f'No Brasil ta {C:.0f}° e nos EUA ta com {F}° Graus, Lá e Fahrenheit !')
