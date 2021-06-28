matriz = []

for i in range(2):
    matriz.append(list(map(int, input().split())))

maior = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento

print(maior)
