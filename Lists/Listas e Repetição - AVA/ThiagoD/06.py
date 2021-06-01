lista = list(map(int, input().split()))
pares = []
impares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
        
print(lista)
print(pares)
print(impares)
