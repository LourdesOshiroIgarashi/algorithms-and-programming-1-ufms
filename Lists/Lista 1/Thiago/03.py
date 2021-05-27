# Leia 20 números inteiros e armazene-os em uma lista. Em seguida, separe os números pares dos ímpares em dois vetores distintos. Imprima os três vetores.

def leitorDeLista():
    lista = list(map(int, input().split()))
    return lista


listaOriginal = leitorDeLista()
listaPares = []
listaImpares = []

for item in listaOriginal:
    if item % 2 == 0:
        listaPares.append(item)
    else:
        listaImpares.append(item)

print(listaOriginal)
print(listaPares)
print(listaImpares)
