idades = list(map(int,input().split()))
alturas = list(map(float,input().split()))
soma = 0
cont = 0

for i in range(0, len(idades), 1):
    if idades[i] >= 13:
        soma += alturas[i]
        cont += 1

if cont != 0:
    media = soma / cont

cont = 0
for i in range(0, len(idades), 1):
    if idades[i] >= 13:
        if alturas[i] <= media:
            cont += 1

print("Idade || Altura")
for i in range(0, len(idades), 1):
    print("{:3d}".format(idades[i]), end ='')
    print("{:11.2f}".format(alturas[i]))

print("\n")
if cont == 0:
    print("Não existem pessoas com 13 anos ou mais nesta amostra.")
else:
    print("Média de altura das pessoas com 13 anos ou mais: {0:.2f}\nExistem {1} pessoas com 13 anos ou mais que estão abaixo da média das pessoas com esta faixa etária".format(media, cont))
