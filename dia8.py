# Dia 8 - While: múltiplos de 10 até 100
x = n = 0
while n <= 100:
    if n % 10 == 0:
        x += 1
    n += 1
print(x)
