n = int(input())

# linhas
for i in range(n):
    # O que se faz em cada linha
    for j in range(i):
        print(" ", end="")
    print(i + 1)
