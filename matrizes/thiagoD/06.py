matriz = []

for i in range(5):
    matriz.append(list(map(int, input().split())))

maiores = []

for linha in range(len(matriz)):
    elementoMaior = 0

    for elemento in range(len(matriz[linha])):
        if matriz[linha][elemento] > matriz[linha][elementoMaior]:
            linhaMaior = linha
            elementoMaior = elemento

    maiores.append([linha, elementoMaior, matriz[linha][elementoMaior]])

for i in range(len(maiores)):
    print(f"M[{maiores[i][0] + 1}][{maiores[i][1] + 1}] = {maiores[i][2]}")
