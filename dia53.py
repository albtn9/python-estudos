# Dia 53 - Gerador de senha segura
import random
import string
try:
    size = int(input("Digite o tamanho de caracteres para a Senha: "))
except ValueError:
    print("Ainda Não posso contar letras")
else:
    if size <= 4:
        print('A senha vai ficar muito fraca')
    elif size >= 25:
        print(f'com esse tamanho aqui : {size}, tu me quebra')
    else:
        lmin = string.ascii_lowercase
        lmai = string.ascii_uppercase
        lnum = string.digits
        lsim = "!@#$%&*?_+-="
        all_chars = lmin + lmai + lnum + lsim
        key = []
        key.append(random.choice(lmin))
        key.append(random.choice(lmai))
        key.append(random.choice(lnum))
        key.append(random.choice(lsim))
        random.shuffle(key)
        faltam = size - len(key)
        for i in range(faltam):
            key.append(random.choice(all_chars))
        senha = ''.join(key)
        print(f'Sua senha Segura com {size} caracteres é : ')
        print(f'{senha}')
