# Leia 2 números e imprima apenas o maior deles.

n1, n2 = map(int, input().split())

if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
else:
    print(f"{n1} = {n2}")
