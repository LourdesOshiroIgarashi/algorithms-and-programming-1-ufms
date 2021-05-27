# Tentando descobrir se um dado é viciado, um jogador o lançou n vezes. Dados os n resultados do lançamento, determine o número de ocorrências de cada face.

def leitorLista():
    lista = list(map(int, input().split()))
    return lista


resultadosLancamento = leitorLista()

face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0

for i in resultadosLancamento:
    if i == 1:
        face1 += 1
    elif i == 2:
        face2 += 1
    elif i == 3:
        face3 += 1
    elif i == 4:
        face4 += 1
    elif i == 5:
        face5 += 1
    elif i == 6:
        face6 += 1

print(f"Número de vezes que o dado caiu com 1 pra cima = {face1}")
print(f"Número de vezes que o dado caiu com 2 pra cima = {face2}")
print(f"Número de vezes que o dado caiu com 3 pra cima = {face3}")
print(f"Número de vezes que o dado caiu com 4 pra cima = {face4}")
print(f"Número de vezes que o dado caiu com 5 pra cima = {face5}")
print(f"Número de vezes que o dado caiu com 6 pra cima = {face6}")
