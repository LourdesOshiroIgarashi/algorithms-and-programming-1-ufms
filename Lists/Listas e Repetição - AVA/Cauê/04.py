lista = list(map(float,input().split()))

media =  sum(lista) / len(lista)

menor = 0
maior = 0

for i in lista:
    if i > media:
        maior += 1
    else:
        menor += 1

print("O valor médio da lista: ", end="")

for i in lista:
    print(i, end=" ")
print(" é: {0:.6f}\n".format(media))
print("Existem {0} valores menores ou iguais a média e {1} valores maiores que a média.".format(menor, maior))
