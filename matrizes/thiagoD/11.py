matriz = []
somasLinha = []
linhasMultiplicadas = []

for linha in range(5):
    matriz.append(list(map(int, input().split())))

    somaLinha = 0
    for i in matriz[linha]:
        somaLinha += i
    somasLinha.append(somaLinha)

    multMatrizSoma = []
    for i in range(len(matriz[linha])):
        multMatrizSoma.append(matriz[linha][i] * somasLinha[linha])
    linhasMultiplicadas.append(multMatrizSoma)

for i in range(len(linhasMultiplicadas)):
    print(
        f"{linhasMultiplicadas[i][0]:8d}{linhasMultiplicadas[i][1]:8d}{linhasMultiplicadas[i][2]:8d}{linhasMultiplicadas[i][3]:8d}{linhasMultiplicadas[i][4]:8d}")
