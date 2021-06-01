def reader():
    return list(input().split())


seq1 = reader()
seq2 = reader()

intercalado = []

for i in range(len(seq1)):
    intercalado.append(seq1[i])
    intercalado.append(seq2[i])

print(f"Sequência 1: {seq1}")
print(f"Sequência 2: {seq2}")
print(f"Itercalação da Sequência 1 e Sequência 2:\n{intercalado}")
