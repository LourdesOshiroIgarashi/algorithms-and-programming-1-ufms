lista = list(map(float, input().split()))

media = sum(lista) / len(lista)

menorQueMedia, maiorQueMedia = 0, 0

for i in lista:
    if i > media:
        maiorQueMedia += 1
    else:
        menorQueMedia += 1

print("O valor médio da lista: ", end="")
for i in lista:
    print(i, end=" ")
print(f" é: {media:.6f}")
print("")

print(f"Existem {menorQueMedia} valores menores ou iguais a média e {maiorQueMedia} valores maiores que a média.")
