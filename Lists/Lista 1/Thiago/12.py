# Leia um número n e determine os 50 primeiros termos da série n, (n - 1), (n - 2), (n - 3), ..., 1.
# Em seguida calcule e imprima o resultado da soma do primeiro termo + último termo, segundo termo + penúltimo termo, terceiro termo + antepenúltimo termo, ...

def soma(lista):
    soma = lista[0] + lista[-1]
    return soma


n = int(input())

serie = []

if n > 50:
    for i in range(50):
        y = n - i
        serie.append(y)
else:
    for i in range(n):
        y = n - i
        serie.append(y)

for i in range(int(len(serie) // 2)):
    print(soma(serie))
    serie.pop(0)
    serie.pop(-1)
