seq1 = list(input().split())
seq2 = list(input().split())

intercalar = []

for i in range(10):
    intercalar.append(seq1[i])
    intercalar.append(seq2[i])

print("Sequência 1: {0}".format(seq1))
print("Sequência 2: {0}".format(seq2))
print("Itercalação da Sequência 1 e Sequência 2:\n{0}".format(intercalar))
