intercalacao = []
sequencia11 = []
sequencia22 = []

sequencia1 = list(map(int, input().split()))
sequencia2 = list(map(int, input().split()))

for i in range(10):
    sequencia11.append('{}'.format(sequencia1[i]))
    sequencia22.append('{}'.format(sequencia2[i]))

for i in range(10):
    intercalacao.append('{}'.format(sequencia1[i]))
    intercalacao.append('{}'.format(sequencia2[i]))

print("Sequência 1: {}".format(sequencia11))
print("Sequência 2: {}".format(sequencia22))
print("Itercalação da Sequência 1 e Sequência 2:")
print(intercalacao)
