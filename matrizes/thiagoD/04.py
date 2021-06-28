matriz = []

for i in range(2):
    matriz.append(list(map(int, input().split())))

linhaMaior, colMaior = 0, 0

for linha in range(len(matriz)):
    for elemento in range(len(matriz[linha])):
        if matriz[linha][elemento] > matriz[linhaMaior][colMaior]:
            linhaMaior, colMaior = linha, elemento

print(
    f"Maior elemento: M[{linhaMaior + 1}][{colMaior + 1}] = {matriz[linhaMaior][colMaior]}")
