n = int(input())
valores = []

for i in range(n):
    k = int(input())
    valores.append(k)

mult3 = []

for i in valores:
    if i % 3 == 0:
        mult3.append(i)

for i in mult3:
    print(i, end=" ")
