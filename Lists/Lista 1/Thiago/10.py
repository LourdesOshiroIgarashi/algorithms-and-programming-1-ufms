# Leia um conjunto de n valores inteiros, para 1 ≤ n ≤ 30, e imprima o elemento central. Para n par,deve-se considerar a existência de 2 elementos centrais.
# Exemplos: na sequência [5, 223, 76, 19, 0,43, 5] o elemento central é 19, já a sequência [44, 6, 89, 6, 2, 5, 77, 43, 27, 94] possui dois elementos centrais: 2 e 5.

def leitorLista():
    lista = list(map(int, input().split()))
    return lista


lista = leitorLista()

if len(lista) % 2 == 1:
    indiceCentro = int(len(lista) / 2)
    print(f"O elemento central do conjunto dado é: {lista[indiceCentro]}")
else:
    indiceCentro1 = int(len(lista) / 2 - 1)
    indiceCentro2 = int(len(lista) / 2)
    print(
        f"O conjunto dado possui 2 elementos centrais: {lista[indiceCentro1]} e {lista[indiceCentro2]}.")
