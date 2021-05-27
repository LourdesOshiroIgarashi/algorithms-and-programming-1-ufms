a, b, c = map(int, input().split(" "))
x, y, z = map(int, input().split(" "))

if x >= a:
    horas = x - a
    if y >= b:
        minutos = y - b
    else:
        minutos = 60 - b + y
        horas = horas - 1

    if z >= c:
        seg = z - c
    else:
        seg = 60 - c + z
        minutos = minutos + 1

else:
    horas = 24 - a + x - 1
    if y >= b:
        minutos = y - b
    else:
        minutos = 60 - b + y - 1

    if z >= c:
        seg = z - c
        minutos = minutos + 1
    else:
        seg = 60 - c + z

print(horas, minutos, seg)
