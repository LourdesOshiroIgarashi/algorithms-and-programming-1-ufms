def convert(n):
    h = n // 3600
    m = n % 3600 // 60
    s = n % 3600 % 60
    return h, m, s


valor = int(input())
h, m, s = convert(valor)

print(f"{valor} segundos equivale a {h}:{m}:{s}")
