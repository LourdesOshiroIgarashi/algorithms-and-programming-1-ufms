def Multiplicacao(matriz, vetor):
    resultado = []

    for linha in matriz:
        multLinha = []

        for i in range(len(linha)):
            multLinha.append(linha[i] * vetor[i])

        resultado.append(multLinha)

    return resultado


matriz = []

for linha in range(3):
    matriz.append(list(map(int, input().split())))

vetor = list(map(int, input().split()))

resultMultiplicacao = Multiplicacao(matriz, vetor)

soma = []

for linha in resultMultiplicacao:
    somaLinha = 0

    for elemento in linha:
        somaLinha += elemento

    soma.append(somaLinha)

for i in soma:
    print(i, end=" ")
