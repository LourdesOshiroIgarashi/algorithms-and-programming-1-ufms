# Leia um texto e faça a impressão deste em ordem inversa. Deve-se implementar
# ao menos as funções inverte() e imprime().

def inverte(s):
    s = s[::-1]
    return s


def imprime(a):
    print(a)


imprime(inverte(input()))
