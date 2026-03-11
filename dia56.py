# Dia 56 - Unidade, dezena, centena, milhar
a = int(input("Digite algo: "))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print('Unidade :', u)
print('Dezena : ', d)
print('Centena : ', c)
print('Milhar : ', m)
