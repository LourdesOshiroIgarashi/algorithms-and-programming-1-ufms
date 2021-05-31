x = list(map(float, input().split(" ")))

soma = 0
for i in x:
    soma = soma + i
media = soma / 11

maiorm = 0
menorm = 0
for i in x:
    if i > media:
        maiorm = maiorm + 1

    else:
        menorm = menorm + 1

print("O valor médio da lista: ", end='')
for i in x:
    print(i, end=" ")
print(" é: {0:.6f}".format(media))
print("")
print("Existem {} valores menores ou iguais a média e {} valores maiores que a média.".format(menorm, maiorm))
