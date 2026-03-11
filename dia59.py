# Dia 59 - Análise da letra A na frase
a = str(input("Digite algo: ")).upper().strip()
print('A letra A apareceu: ', a.count('A'), 'X na Frase')
print('A letra A apareceu a primeira vez em:', a.find('A')+1)
print('A letra A apareceu a última vez em:', a.rfind('A')+1)
