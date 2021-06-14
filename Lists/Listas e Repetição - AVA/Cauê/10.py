lista = list(map(int, input().split()))

for i in lista:
    print(i, end=" ")

if len(lista) % 2 == 0:
    print(f"\nElementos centrais da lista: {lista[(len(lista) // 2 - 1)]} e {lista[(len(lista) // 2)]}")
else:
    print(f"\nElemento central da lista: {lista[(len(lista) // 2)]}")
