# Dia 7 - Categoria do lutador (peso)
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
print(f'Lutador : {nome} Peso : {peso}')
if peso < 52:
    categoria = 'Invalida'
elif peso < 65:
    categoria = 'Pena'
elif peso < 72:
    categoria = 'Leve'
elif peso < 79:
    categoria = 'Ligeiro'
elif peso < 86:
    categoria = 'Meio-médio'
elif peso < 90:
    categoria = 'Médio'
elif peso < 100:
    categoria = 'Meio-pesado'
else:
    categoria = 'Pesado'
print(f'O {nome} pesa {peso:.3f}kg e vai para a Categoria {categoria}')
