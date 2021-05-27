# Leia 11 números inteiros e, em seguida, calcule a média destes números.

def leitorDeLista():
    lista = list(map(int, input().split()))
    return lista


lista = leitorDeLista()
media = sum(lista) / len(lista)
print(f"A média da lista dada é {media:.2f}")
