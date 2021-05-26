medias = []

for i in range(6):
    soma = 0
    for j in range(3):
        soma += float(input())
    media = soma/3
    medias.append(medias)

maiorm = 0
for i in medias:
    if i >= 7:
        maiorm += 1
print(maiorm)
