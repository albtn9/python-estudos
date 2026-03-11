# Dia 17 - Try/except (divisão e ValueError)
try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(R)
except ZeroDivisionError:
    print('Não pode dividir por zero')
except ValueError:
    print('Digite valores Inteiros')
except Exception:
    print('deu um erro')
