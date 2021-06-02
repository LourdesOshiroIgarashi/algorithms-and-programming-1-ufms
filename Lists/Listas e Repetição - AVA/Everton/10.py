serie = list(map(int, input().split()))


for i in range(0, len(serie), 1):
    print(serie[i], end = ' ')


if len(serie)%2 == 0:
    print("\nElementos centrais da lista: {1} e {0}".format(serie[(len(serie)//2)], serie[(len(serie)//2-1)]))

else:
    print("\nElemento central da lista: {}".format(serie[len(serie)//2]))

