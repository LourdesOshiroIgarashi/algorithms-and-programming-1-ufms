# r = 2, a = 5, b = 6, c = 7 -- Cabe | r = 2.6, a = 2.8, b = 5, c = 5 -- Não cabe
# r = 6, a = 13, b = 11, c = 13 -- Não cabe | r = 3, a = 7.4, b = 6.1, c = 6 -- Cabe

# d = 2*r | A questão dizia "dado o diâmetro"
d = float(input())
a, b, c = map(float, input().split())

if a >= d and b >= d and c >= d:
    print("S")
else:
    print("N")
