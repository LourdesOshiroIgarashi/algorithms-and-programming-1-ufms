n = int(input())
valores = []

for i in range(n):
    k = int(input())
    valores.append(k)

for v in range(len(valores)):
    print(f"{valores[v]}! = ", end="")
    for f in range(valores[v], 0, -1):
        if f == 1:
            print(f)
        else:
            print(f, end=" * ")
