# Dia 15 - Soma e quantidade de valores (0 para encerrar)
soma = qtde = 0
A = int(input('Digite um valor: '))
while A != 0:
    soma = soma + A
    qtde = qtde + 1
    A = int(input('Digite um valor: '))
print(f'Soma dos Valores: {soma}')
print(f'Quantidade de Valores: {qtde}')
print('Fim do Programa')
