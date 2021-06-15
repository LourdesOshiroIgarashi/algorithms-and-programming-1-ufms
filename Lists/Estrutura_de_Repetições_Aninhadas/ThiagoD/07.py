n = int(input())

# controla as linhas
for linha in range(1, n + 1):
    n -= 1
    for i in range(n, 0, -1):
        print(" ", end="")
    for j in range(linha):
        print("+", end=" ")
    print("")
