x = int(input())

serie = []

for i in range(1, 101, 1):
    serie.append((i*(x**i)/(i**2)))

media = 0
for i in serie:
    media += i
media = media / 100

menorm = 0
for i in serie:
    if i < media:
        menorm += 1
print(menorm)
