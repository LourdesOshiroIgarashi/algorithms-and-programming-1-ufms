matriz = []

for i in range(4):
    matriz.append(list(map(int, input().split())))

linhaMenorElemento = 0
menorElemento = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < menorElemento:
            menorElemento = matriz[i][j]
            linhaMenorElemento = i

colunaMaiorElementoMenorLinha = 0
for i in range(len(matriz[linhaMenorElemento])):
    if matriz[linhaMenorElemento][i] > matriz[linhaMenorElemento][colunaMaiorElementoMenorLinha]:
        colunaMaiorElementoMenorLinha = i

print(matriz[linhaMenorElemento][colunaMaiorElementoMenorLinha],
      linhaMenorElemento, colunaMaiorElementoMenorLinha)
