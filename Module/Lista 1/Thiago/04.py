# Leia um inteiro e determine o valor de a^2, 2^a e a^a. Implemente três
# funções distintas para realizar os cálculos descritos.

def pot1(a):
    return a ** 2


def pot2(a):
    return 2 ** a


def pot3(a):
    return a ** a


n1 = int(input())

aAoQuadrado = pot1(n1)
doisElevadoAa = pot2(n1)
aElevadoAa = pot3(n1)

print(aAoQuadrado, doisElevadoAa, aElevadoAa)
