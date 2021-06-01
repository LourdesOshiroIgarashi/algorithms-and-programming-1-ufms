Lista = []
soma = 0

for i in range(15):
    Lista.append(float(input()))

print(Lista)

for i in Lista:
    soma += i

print(soma/15)
