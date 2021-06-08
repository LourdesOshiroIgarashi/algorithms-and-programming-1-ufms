medias = []

for i in range(6):
    x, y, z = map(float, input().split())
    soma = x + y + z
    media = soma/3
    medias.append(media)

maiorm = 0
for i in medias:
    if i >= 7:
        maiorm += 1

print("Médias")
for i in range(6):
    print("Média do aluno {}: {}".format(i + 1, round(medias[i],3)))

print("Existem {} alunos com média maior ou igual a 7.0".format(maiorm))
