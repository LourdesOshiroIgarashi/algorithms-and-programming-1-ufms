# Leia 10 valores numéricos e, em seguida, calcule a média destes números bem como a quantidade de números lidos que é menor do que a média.

def leitorDeLista():
    lista = list(map(float, input().split()))
    return lista


lista = leitorDeLista()
media = sum(lista) / len(lista)
nMenorQueMedia = 0

for n in lista:
    if n < media:
        nMenorQueMedia = nMenorQueMedia + 1

print(f"Lista = {lista}")
print(f"Média = {media:.2f}")
print(f"Quantidade de números na lista menores que a média = {nMenorQueMedia}")
