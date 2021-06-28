notas = []
numAlunoMenorNota = []
numMenorProva = [0, 0, 0]

for i in range(10):
    notas.append(list(map(float, input().split())))

    menorNota = notas[i][0]
    posicaoMenorNota = 1

    for elem in range(len(notas[i])):
        if notas[i][elem] < menorNota:
            menorNota = notas[i][elem]
            posicaoMenorNota = elem + 1

    if posicaoMenorNota == 1:
        numMenorProva[0] += 1
    elif posicaoMenorNota == 2:
        numMenorProva[1] += 1
    else:
        numMenorProva[2] += 1

    append = [i + 1, posicaoMenorNota]
    numAlunoMenorNota.append(append)

for i in range(len(numAlunoMenorNota)):
    for j in numAlunoMenorNota[i]:
        print(j, end=" ")

for i in numMenorProva:
    print(i, end=" ")
