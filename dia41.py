# Dia 41 - Seno, cosseno e tangente (ângulo)
import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
print(f'o angulo de {ang} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(ang))
print(f'o angulo de {ang} tem o cosseno de {cosseno:.2f}')
tange = math.tan(math.radians(ang))
print(f'o angulo de {ang} tem a tangente de {tange:.2f}')
