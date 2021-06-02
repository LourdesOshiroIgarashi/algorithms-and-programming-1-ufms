n = int(input())

seq1 = []

for i in range(n):
    x = n
    seq1.append(x)
    n -= 1
seq1cheia = list(seq1)
seq2 = []

for i in range(len(seq1) // 2):
    valor = seq1[0] - seq1[-1]
    seq1.pop(0)
    seq1.pop(-1)
    seq2.append(valor)

print(seq1cheia)
print(seq2 + seq1)
