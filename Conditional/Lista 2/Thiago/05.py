import math


def read():
    x = int(input())
    return x


nAlunos = read()
nMonitores = read()
total = nAlunos + nMonitores

if total <= 50:
    print("Todos podem subir juntos!")
else:
    nViagens = math.ceil(total / 50)
    print(
        f"São necessárias no mínimo {nViagens} viagens para levar todos vocês!")
