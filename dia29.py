# Dia 29 - Filtro em lista (for)
LISTA = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
A = []
for i in LISTA:
    if i > 60 and i < 140:
        A.append(i)
print(A)
