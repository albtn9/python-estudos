# Dia 6 - Menor de dois números
X = int(input('Digite um valor: '))
Y = int(input('Digite outro valor: '))
if X == Y:
    print(f'Os números {X} e {Y} são iguais')
else:
    if X < Y:
        print(f'O menor número é {X}')
    else:
        print(f'o menor número é {Y}')
