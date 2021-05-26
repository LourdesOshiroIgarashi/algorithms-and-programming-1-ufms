n = int(input('n: '))
idades = []
alturas = []

for i in range(30):
    idades.append(int(input()))
    alturas.append(int(input()))

media = 0
for i in alturas:
    media += i
media /= n

inferiorm = 0
for i in range(30):
    if idades[i] > 13:
        if alturas[i] < media:
            minferiorm += 1

#  print(idades)
#  print(alturas)
#  print(media)

print(inferiorm)
