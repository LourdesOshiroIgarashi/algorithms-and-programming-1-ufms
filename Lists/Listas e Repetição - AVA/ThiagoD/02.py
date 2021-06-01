lista = list(map(int, input().split()))

for item in lista:
    print(item, end=" ")

print("\n")

for item in lista[::-1]:
    print(item, end=" ")
