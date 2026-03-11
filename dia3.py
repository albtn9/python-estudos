# Dia 3 - Classificação de pH
PH = float(input('Digite o pH :'))
if PH < 6.0:
    r = 'acido'
elif PH < 7.0:
    r = 'levemente acido'
elif PH == 7.0:
    r = 'neutro'
elif PH < 8.0:
    r = 'levemente alcalina'
else:
    r = 'alcalina'
print(f'Com pH = {PH} a solução é {r}')
