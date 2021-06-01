medias = []

for i in range(6):
    a, b ,c = map(float,input().split())
    somaNotas = a + b + c
    media = somaNotas/3
    medias.append(media)

maiorMedia = 0
for i in medias:
    if i >= 7:
        maiorMedia += 1

print("Médias")
for i in range(6):
    print("Média do aluno {}: {}".format(i + 1, round(medias[i],3)))

print("Existem {} alunos com média maior ou igual a 7.0".format(maiorMedia))
