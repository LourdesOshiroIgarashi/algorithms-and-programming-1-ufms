matriz1 = []
for i in range(4):
    matriz1.append(list(map(int, input(
        f"Digite os 5 elementos da linha {i + 1} divididos por espaço: ").split())))

matriz2 = []
for i in range(5):
    matriz2.append(list(map(int, input(
        f"Digite os 2 elementos da linha {i + 1} divididos por espaço: ").split())))

result = []

for i in range(len(matriz1)):
    soma1, soma2 = 0, 0
    for j in range(len(matriz2)):
        soma1 += matriz1[i][j] * matriz2[j][0]
        soma2 += matriz1[i][j] * matriz2[j][1]

    result.append([soma1, soma2])

for i in result:
    for j in i:
        print(j, end=" ")
    print()
