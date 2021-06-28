matriz = []

for i in range(2):
    matriz.append(list(map(int, input().split())))

menor = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento < menor:
            menor = elemento

print(menor)
