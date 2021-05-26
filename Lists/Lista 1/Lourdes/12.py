n = int(input())

serie = []

for i in range(50):
    serie.append(n-i)

for i in range(25):
    print(serie[i] + serie[-i])
