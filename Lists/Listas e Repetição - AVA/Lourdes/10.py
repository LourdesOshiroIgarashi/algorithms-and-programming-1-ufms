lista = list(map(int, input().split()))
x = len(lista)

for i in lista:
    print(i, end=" ")

if x % 2 == 0:
    y1 = (x // 2) - 1
    y2 = x // 2
    print("\nElementos centrais da lista: {} e {}".format(lista[y1], lista[y2]))
else:
    y1 = x // 2
    y1 = int(y1)
    print("\nElemento central da lista: {}".format(lista[y1]))
