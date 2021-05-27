# Leia uma lista de 10 números reais e, em seguida, mostre-os na ordem inversa.

def leitorDeLista():
    lista = list(map(int, input().split()))
    return lista


lista = leitorDeLista()
print(lista[::-1])
