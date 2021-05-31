x = []

for i in range(15):
    x.append(float(input()))

print(x)

soma = 0
for i in x:
    soma = soma + i

print(soma/15)
