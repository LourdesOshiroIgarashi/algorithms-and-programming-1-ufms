# Leia dois inteiros, a e b, e informe ao usuário se a é múltiplo de b

a, b = map(int, input().split())

if a % b == 0:
    print(f"{a} é múltiplo de {b}")
else:
    print(f"{a} não é múltiplo de {b}")
