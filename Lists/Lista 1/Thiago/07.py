# Leia duas sequências numéricas de tamanho 10 cada. Apresente o resultado da intercalação da primeira sequência lida com a segunda e vice-versa.

def leitorLista():
    lista = list(map(int, input().split()))
    return lista


lista1 = leitorLista()
lista2 = leitorLista()

listaIntercalada = []

for i in range(len(lista1)):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])

print(lista1)
print(lista2)
print(listaIntercalada)
