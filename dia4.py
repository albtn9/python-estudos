# Dia 4 - Grau de risco e tipo de investimento
risco = input('Digite BX ou AL para o grau de risco : ')
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é invalido para o grau de risco')
else:
    valor = float(input('Digite o valor do risco R$ '))
    if risco == 'BX':
        if valor < 1000.0:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000.0:
            tipo = 'BitCoins'
        else:
            tipo = 'Ações'
    print(f'Voce deve investir em {tipo}')
