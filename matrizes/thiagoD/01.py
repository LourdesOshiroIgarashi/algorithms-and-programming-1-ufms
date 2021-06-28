linhas = int(input())
colunas = int(input())

matriz = []

for linha in range(linhas):
    linha = list(map(int, input().split()))
    for i in range(len(linha)):
        linha[i] *= 2
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print("")
