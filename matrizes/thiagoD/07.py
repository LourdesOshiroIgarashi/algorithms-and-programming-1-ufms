matriz = []

for i in range(5):
    matriz.append(list(map(int, input().split())))

somas = []

for linha in matriz:
    somaLinha = 0
    for elemento in linha:
        somaLinha += elemento

    somas.append(somaLinha)


aux = somas[0]
linhaMaior = 1
for i in range(len(somas)):
    if somas[i] > aux:
        aux = somas[i]
        linhaMaior = i + 1


print("Vetor correspondente à soma dos elementos de cada uma das linhas da matriz:")
for i in somas:
    print(i, end=" ")

print()

print("Linha cuja soma dos elementos é a maior dentre todas as linhas:")
print(linhaMaior)
