lista = list(map(int, input().split()))

for item in lista:
    print(item, end=" ")

lista = lista[::-1]
print("\n")

for item in lista:
    print(item, end=" ")
