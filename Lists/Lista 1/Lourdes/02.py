notas = []

for i in range(4):
    notas.append(float(input()))
    print(notas)

media = ( notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(media)
