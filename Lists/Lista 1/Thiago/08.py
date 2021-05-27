# Leia as informações de idades e alturas de 30 pessoas. Determine quantas pessoas com mais de 13 anos possuem altura inferior à média das alturas.

def leitorLista():
    lista = list(map(int, input().split()))
    return lista


def media(lista):
    media = sum(lista) / len(lista)
    return media


listaCompleta = leitorLista()
idades = listaCompleta[::2]
alturas = listaCompleta[1::2]

mediaAlturas = media(alturas)

anoes = 0

for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < mediaAlturas:
        anoes += 1


print(f"Idades seguidas das alturas em cm = {listaCompleta}")
print(f"Idades = {idades}")
print(f"Alturas em cm = {alturas}")
print(
    f"Quantidade de pessoas com mais de 13 anos e altura inferior à média = {anoes}")
