# Dia 50 - Dicionário (values)
pessoas = {"nome": "Joao", "idade": 22, "sexo": "M"}
for chave in pessoas.values():
    print(str(chave).upper())
    x = int(pessoas["idade"]) + 1
    print(x)
