# Leia dois valores, a e b. Se os valores forem iguais, some-os, caso contrário, multiplique-os.

a, b = map(int, input().split())

if a == b:
    print(a + b)
else:
    print(a * b)
