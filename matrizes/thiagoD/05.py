matriz = []

for i in range(2):
    matriz.append(list(map(int, input().split())))

linhaMenor = 0
colunaMenor = 0

for linha in range(len(matriz)):
    for elemento in range(len(matriz[linha])):
        if matriz[linha][elemento] < matriz[linhaMenor][colunaMenor]:
            linhaMenor = linha
            colunaMenor = elemento

print(
    f"Menor elemento: M[{linhaMenor + 1}][{colunaMenor + 1}] = {matriz[linhaMenor][colunaMenor]}")
