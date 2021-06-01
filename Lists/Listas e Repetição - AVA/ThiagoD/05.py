def readList():
    return list(map(float, input().split()))


medias = []
for i in range(6):
    notaAluno = readList()
    mediaAluno = round((sum(notaAluno) / 3), 3)
    medias.append(mediaAluno)

passados = 0
for i in medias:
    if i >= 7:
        passados += 1
    else:
        continue

print("Médias")
for i in range(len(medias)):
    print(f"Média do aluno {i + 1}: {medias[i]}")

print(f"Existem {passados} alunos com média maior ou igual a 7.0")
