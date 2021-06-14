n = int(input())

lista = ["+"]
x = "+"
aux = n
# controla as linhas
for linha in range(1, n + 1):
    aux -= 1
    for i in range(aux, 0, -1):
        print(" ", end="")
    for j in range(linha):
        print(x, end=" ")
    print("")
