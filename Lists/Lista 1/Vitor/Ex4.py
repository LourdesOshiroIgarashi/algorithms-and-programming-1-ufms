#Entrada
notas = list(map(int,input("Digite 11 números inteiros: ").split(" ")))
#Processamento
soma = 0
for i in notas:
    soma = soma + i
media = soma/len(notas)
#Saída
print("A média é {}.".format(media))