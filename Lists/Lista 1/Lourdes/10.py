lista = []

n = int(input())

for i in range(n):
    lista.append(int(input()))
print(lista)

if n % 2 == 0:
    elemento1 = n//2 - 1
    elemento2 = n//2
    print(lista[elemento1], lista[elemento2])
else:
    elemento = n//2
    print(lista[elemento])
