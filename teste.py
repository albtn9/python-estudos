# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))
# r = a + b
# print("A soma de {} e {} resulta em {}".format(a,b,r))

# A = int(input('Digite o valor de A: '))
# B = int(input('Digite o valor de B: '))
# if A == 0 or B == 0 :
#     print('Não é possivel calcular a divisão')
# else :
#     R = A / B
#     print('A Divisão é :',R)

# PH = float(input('Digite o pH :'))
# if PH < 6.0:
#     r = 'acido'
# elif PH < 7.0:
#     r = 'levemente acido'
# elif PH == 7.0:
#     r = 'neutro'
# elif PH < 8.0:
#     r = 'levemente alcalina'
# else  :
#     r = 'alcalina'
# print(f'Com pH = {PH} a solução é {r}')

# risco = input('Digite BX ou AL para o grau de risco : ')
# if risco != 'BX' and risco != 'AL':
#     print(f'{risco} é invalido para o grau de risco')
# else:
#     valor = float(input('Digite o valor do risco R$ '))
#     if risco == 'BX':
#         if valor < 1000.0:
#             tipo = 'Poupança'
#         else:
#             tipo = 'Renda Fixa'
#     else :
#         if valor < 1000.0:
#             tipo = 'BitCoins'
#         else:
#             tipo = 'Ações'
#     print(f'Voce deve investir em {tipo}')
#
# Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. Lembrando
# que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2. Se o resto for
# 0 o número é par, se o resto for 1 o número é ímpar

# numero = int(input('Digite um número : '))
# if numero % 2 == 0:
#     print(f'{numero} é Par')
# else:
#     print(f'{numero} é Impar')

# Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos
# forem iguais, mostre qualquer um deles

# X = int(input('Digite um valor: '))
# Y = int(input('Digite outro valor: '))
# if X == Y:
#     print(f'Os números {X} e {Y} são iguais')
# else :
#     if X < Y:
#         print(f'O menor número é {X}')
#     else:
#         print(f'o menor número é {Y}')

# Escreva um programa para exibir na tela o nome e a categoria de um lutador. O programa deve ler
# um string para o nome e um número real para o peso. Conforme o peso ocorrerá o enquadramento
# na categoria, segundo esta tabela (fictícia):

# nome = input('Digite seu nome: ')
# peso = float(input('Digite seu peso: '))
# print(f'Lutador : {nome} Peso : {peso}')
# if peso < 52:
#     categoria = 'Invalida'
# elif peso < 65:
#     categoria = 'Pena'
# elif peso < 72:
#     categoria = 'Leve'
# elif peso < 79:
#     categoria = 'Ligeiro'
# elif peso < 86:
#     categoria = 'Meio-médio'
# elif peso < 90:
#     categoria = 'Médio'
# elif peso < 100:
#     categoria = 'Meio-pesado'
# else :
#     categoria = 'Pesado'
# print(f'O {nome} pesa {peso:.3f}kg e vai para a Categoria {categoria}')

# x = n = 0
# while n <= 100:
#     if n % 10 == 0:
#         x += 1
#     n += 1
# print(x)

# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# x = 1
# while True:
#     x = int(input('Digite X: '))
#     if x == 0 :
#         break
#     print(x)
# print('Fim')

# X = 1
# while X > 0:
#     X = int(input('Digite um valor: '))
#     if X == 0:
#         print('   Digitou Zero...')
#         break
# else:
#     print('   Digitou Negatiovo...')
# print('Fim do programa')

# X = 1
# while X != 0:
#     X = int(input('Digite um valor: '))
#     if X % 2 == 0:
#         print(f'{X} é Par')
#     else :
#         print(f'{X} é Impar')
# print('Fim do programa')

# X = int(input('Digite um valor: '))
# Y = 1
# while Y <= 10:
#     print(f'{X} x {Y} = {Y * X}')
#     Y += 1

# P = int(input('Digite o primeiro numero: '))
# R = int(input('Digite a Razão: '))
# cont = 1
# while cont  <= 10:
#     print(P, end=' - ')
#     P = P + R
#     cont += 1

# D = int(input('Digite o Valor:'))
# if D <= 0:
#     print('Fim do Programa')
# else:
#     i = 1
#     while i < 100:
#         if i % D == 0:
#             print(i, end='  ')
#         i += 1
# print('\n\nFim do Programa')

# soma = qtde = 0
# A = int(input('Digite um valor: '))
# while A != 0:
#     soma = soma + A
#     qtde = qtde + 1
#     A = int(input('Digite um valor: '))
# print(f'Soma dos Valores: {soma}')
# print(f'Quantidade de Valores: {qtde}')
# print('Fim do Programa')

# a = 0
# b = 10
# c = 0
# while a < b:
#   a += 1
#   b -= 2
#   c += b - a
#   print(c)

# try:
#     A = int(input('Digite A: '))
#     B = int(input('Digite B: '))
#     R = A / B
#     print(R)
# except ZeroDivisionError:
#     print('Não pode dividir por zero')
# except ValueError:
#     print('Digite valores Inteiros')
# except:
#     print('deu um erro')

# A = int(input('Digite um valor: '))
# print(f'Analizando o valor: {A}, o dobro dele é  {A * 2} o triplo é {A * 3} e a raiz é {A**(1/2):.2f}')

# A = int(input('Digite um valor: '))
# print(f'Analizando o valor: {A}, o dobro dele é  {A * 2} o triplo é {A * 3} e a raiz é {pow(A,(1/2)):.2f}')

# N1 = float(input('Digite a Primeira Nota do Aluno : '))
# N2 = float(input('Digite a Segunda Nota do Aluno : '))
# M = float(N1 + N2) / 2
# print('A nota da N1 {:.1f} e N2 {:.1f} deram a média de {:.1f}'.format(N1, N2, M))

# L = [44,38,398,578,39,68,11,5,19]
# print('Exibição da lista')
# print(L)
# print('Exibição da lista individual')
# i=0
# while i < len(L):
#     print(L[i], end='   ')
#     i = i + 1
# print('\nFim da lista')

# metro = float(input("Digite um valor em metros: "))
# km = metro / 1000
# print(f'km de {km} ')
# hm = metro / 100
# print(f'hm de {hm} ')
# dec = metro / 10
# print(f'dec de {dec} ')
# print(f'metro de {metro} ')
# dm = metro * 10
# print(f'dm de {dm} ')
# cm = metro * 100
# print(f'cm de {cm} ')
# mm = metro * 1000
# print(f'mm de {mm} ')

# N1 = int(input('Descubra a tabuada de : '))
# i = 1
# while i <= 10:
#     print(f'{N1} x {i} = {N1*i}')
#     i += 1
# print('Fim')

# num = int(input('Digite um número para ver a sua tabuada: '))
# print('-'*18)
# print('{} x {:2} = {}'.format(num , 1, num * 1))
# print('{} x {:2} = {}'.format(num ,2, num * 2))
# print('{} x {:2} = {}'.format(num , 3 ,num*3))
# print('{} x {:2} = {}'.format(num , 4 ,num*4))
# print('{} x {:2} = {}'.format(num,5,num*5))
# print('{} x {:2} = {}'.format(num,6,num*6))
# print('{} x {:2} = {}'.format(num,7,num*7))
# print('{} x {:2} = {}'.format(num,8,num*8))
# print('{} x {:2} = {}'.format(num,9,num*9))
# print('{} x {} = {}'.format(num,10,num*10))

# USD = float(5.38)
# valorBR = float(input("Digite o Valor da Sua Carteira R$: "))
# valor = valorBR / USD
# print(f'em dolar você tem {valor:.2f} USD')

# a = float(input('Digite a largura da parede: '))
# b = float(input('Digite a altura da parede: '))
# c = a * b
# # d = c / 2
# print(f'Sua parede tem a dimensão de {a}x{b} e sua área é de {c}m².')
# # print(f'para pintar essa parede , você precisa de {d}l de tinta')


# P = int(input('Digite o primeiro numero: '))
# R = int(input('Digite a Razão: '))
# Q = int(input('Digite a Quantidade:'))
# Termos = []
# a = 0
# while a  < Q:
#     Termos.append(P)
#     print(P, end=',')
#     P = P + R
#     a += 1
# print('\nLista resultante')
# print('\nFim do Programa')

# e1 = [1, 2, 3, 4]
# e2 = [4, 5, 6]
# r = e1 + e2
# print(r)

# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')

# LISTA = [40, 50, 60, 70, 80, 90, 100,110,120, 130 ,140,150]
# A = []
# for i in LISTA:
#     if i > 60 and i < 140 :
#         A.append(i)
# print(A)

# c1 = {8 ,9.0 ,10, 10.001, 8.0}
# print(c1)
# print(len(c1))

# A = int(input('Digite um Número: '))
# if A % 2 == 0:
#      print('Esse número é Par')
# else:
#      print('Esse número é Impar')
# print('Fim do Programa')
#
# N1 = int(input('Digite o Primeiro numero: '))
# N2 = int(input('Digite o Segundo numero: '))
# R = N1 + N2
# print(f'A soma é : {R}')
# print('Fim do Programa')

# import time
# A = int(input('Digite o Número da Contagem :'))
# while A >= 1:
#     print(A)
#     time.sleep(1)
#     A -= 1
# print('Decolar!')
# print('Fim do Programa')

# valorproduto = float(input("Digite o valor do produto: "))
# R = valorproduto - (valorproduto * 5/100)
# print(f'O Valor do produto com 5% desconto é de {R:.2f}.')

# sAtual = float(input('Qual é o salário do Funcionario: R$'))
# r = sAtual + (sAtual * 15/100)
# print(f'O Salário do Funcionario com 15% de Aumento vai para : {r:.2f}')

# valor = float(input("Digite o valor do produto: "))
# avista = valor - (valor * 10/100)
# print(f'o valor a vista fica em {avista} com 10% de desconto')
# aprazo = valor + (valor * 8/100)
# print(f'o valor a prazo fica em {aprazo} com 8% de acréscimo')

# C = float(input('Quantos Graus ta no Brasil : '))
# F = 9*C /5 +32
# if F < 45:
#     print('Até que ta frio')
# elif F < 75:
#     print('Até que ta bom')
# else:
#     print('Ai tá quente')
# print(f'No Brasil ta {C:.0f}° e nos EUA ta com {F}° Graus, Lá e Fahrenheit !')

# dias = int(input('Quantos dias alugados? '))
# km = float(input('Quantos km rodados? '))
# pago = (dias * 60) + (km * 0.15)
# print(f'o total a pagar é de R${pago:.2f}')

# from math import trunc
#
# num = float(input(f'Digite Um Valor: '))
# valor = math.trunc(num)
# print(f'o valor digitado é {num} inteiro seria {valor}')

# from math import hypot
#
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hi = math.hypot(co, ca)
# print(f'A hipotenusa vai medir {hi:.2f}')

# from math import radians,sin,cos,tan
# # ang = float(input('Digite um angulo: '))
# # seno = sin(radians(ang))
# # print(f'o angulo de {ang} tem o seno de {seno:.2f}')
# # cosseno = cos(radians(ang))
# # print(f'o angulo de {ang} tem o cosseno de {cosseno:.2f}')
# # tange = tan(radians(ang))
# # print(f'o angulo de {ang} tem a tangente de {tange:.2f}')

# from math import sqrt
# num = int(input('Digite um numero : '))
# raiz = sqrt(num)
# print(f'A raiz de {num} é igual a {raiz}')

# import random
# num2 = int(input('Digite um numero : '))
# num2 = random.randint(1, num2)

# import random
# n1 = str(input('Primeiro Aluno: '))
# n2 = str(input('Segundo Aluno: '))
# n3 = str(input('Terceiro Aluno: '))
# n4 = str(input('Quarto Aluno: '))
# sorteio = random.choice([n1,n2,n3,n4])
# print(f'O aluno sorteado foi o {sorteio}')

# import random
#
# n1 = str(input('Primeiro Aluno: '))
# n2 = str(input('Segundo Aluno: '))
# n3 = str(input('Terceiro Aluno: '))
# n4 = str(input('Quarto Aluno: '))
# n5 = str(input('Quinto Aluno: '))
# n6 = str(input('Sexto Aluno: '))
#
# aluno = [n1,n2,n3,n4,n5,n6]
# random.shuffle(aluno)
# print(f'O Primeiro aluno a apresentar é o {aluno[0]}')
# print(f'O Segundo aluno a apresentar é o {aluno[1]}')
# print(f'O Terceiro aluno a apresentar é o {aluno[2]}')
# print(f'O Último aluno a apresentar é o {aluno[3]}')
# print(f'O Não apresentam {aluno[4]} e {aluno[5]}')

# import pygame
#
# pygame.init()
# print(f'tocando')
# pygame.mixer.music.load('1.mp3')
# pygame.mixer.music.play()
# input()
# print(f'Fim')

# a = int(input())
# b = int(input())
# x = a + b
# print('SOMA = ', x)

# LISTA = [1,2,3,4,5,6]
# for iterador in reversed(LISTA):
#     print(iterador)
# print("FIM")

# TUPLA = (1,2,3,4,5,6)
# for iterador in TUPLA:
#     print(iterador)
# print("FIM")

# pessoas = {"nome":"Joao", "idade" : 22, "sexo" : "M"}
#
# for chave in pessoas.values():
#     print(str(chave).upper())
#     x = int(pessoas["idade"]) + 1
#     print(x)

# frase = 'Curso em Vídeo Python'

# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())
# print(frase.title())
# print(frase.count('o'))
# print(frase.find('deo'))

# nome = str(input('Digite seu Nome : ')).strip()
# print('Analisando seu nome...')
# print(nome.upper())
# print(nome.lower())
# print(len(nome)-nome.count(' '))
# separa = nome.split()
# print(f'Seu nome é {separa[0]} e tem {len(separa[0])} letras')

# valor = 0
# for iterador  in range(10) :
#     valor += 1
#     print(valor)
#
# import random
# import string
# #gerar senha
#
# try :
#     size = int(input("Digite o tamanho de caracteres para a Senha: "))
# except ValueError:
#     print("Ainda Não posso contar letras")
# else:
#     if size <= 4:
#             print('A senha vai ficar muito fraca')
#     elif size >= 25:
#         print(f'com esse tamanho aqui : {size}, tu me quebra')
#     else:
#             lmin = string.ascii_lowercase
#             lmai = string.ascii_uppercase
#             lnum = string.digits
#             lsim = "!@#$%&*?_+-="
#             all = lmin + lmai + lnum + lsim
#             key = []
#
#             key.append(random.choice(lmin))
#             key.append(random.choice(lmai))
#             key.append(random.choice(lnum))
#             key.append(random.choice(lsim))
#             random.shuffle(key)
#
#             faltam = size - len(key)
#             for i in range(faltam):
#                 key.append(random.choice(all))
#
#             senha = ''.join(key)
#             print(f'Sua senha Segura com {size} caracteres é : ')
#             print(f'{senha}')

# algum_numero = int(input('digite um número : '))
# for vezes in range(algum_numero):
#     vezes = vezes + 1
#     print(vezes)

# quantos_numeros_tiver = [1,2,3,4,5,6,7,8,9]
#
# for aqui_vai_passar_cada_vez in quantos_numeros_tiver:
#     print(aqui_vai_passar_cada_vez)

# dir()

import math

# a = int(input("Digite algo: "))
# u = a // 1 % 10
# d = a // 10 % 10
# c = a // 100 % 10
# m = a // 1000 % 10
# print(f'Unidade :' , u)
# print(f'Dezena : ',d)
# print(f'Centena : ', c)
# print(f'Milhar : ',m)

# c = str(input('Digite a cidade :')).strip()
# print(c[:5].upper() == 'SANTO')

# c = str(input('Digite seu Nome :')).strip()
# print('SILVA' in c.upper())

# a = str(input("Digite algo: ")).upper().strip()
# print('A letra A apareceu: ',a.count('A'),'X na Frase')
# print('A letra A apareceu a primeira vez em:',a.find('A')+1)
# print('A letra A apareceu a última vez em:',a.rfind('A')+1)
