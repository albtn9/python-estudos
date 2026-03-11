# Dia 20 - Exibição de lista com while
L = [44, 38, 398, 578, 39, 68, 11, 5, 19]
print('Exibição da lista')
print(L)
print('Exibição da lista individual')
i = 0
while i < len(L):
    print(L[i], end='   ')
    i = i + 1
print('\nFim da lista')
