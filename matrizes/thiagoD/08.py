matriz = []

# número de linhas
for i in range(3):
    matriz.append(list(map(int, input().split())))

somas = []

for linha in matriz:
    soma = 0

    # Soma os elementos de cada linha e armazena o valor na variável soma
    for elemento in linha:
        soma += elemento

    # Adiciona a soma total de uma linha à lista somas
    somas.append(soma)

menorSoma = somas[0]
posicaoMenorSoma = 0

# Calcula o menor elemento de somas (menorSoma) e guarda a posição dele (posicaoMenorSoma)
for i in range(len(somas)):
    if somas[i] < menorSoma:
        menorSoma = somas[i]
        posicaoMenorSoma = i + 1

print("Vetor correspondente à soma dos elementos de cada uma das linhas da matriz:")
for i in somas:
    print(i, end=" ")

print()

print("Linha cuja soma dos elementos é a menor dentre todas as linhas:")
print(posicaoMenorSoma)
