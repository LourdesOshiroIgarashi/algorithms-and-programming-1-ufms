valor = []
soma = 0
menor = 0

for i in range(10):
    valor.append(float(input()))

for i in valor:
    soma = soma + i

for i in valor:
    if i < 7:
        menor = menor + 1

n = len(valor)
