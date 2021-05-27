def sep(n):
    num = n

    n1 = n % 10
    num = n // 10

    n2 = num % 10
    num = num // 10

    n3 = num % 10
    num = num // 10

    n4 = num % 10
    return n1, n2, n3, n4


def calc(n1, n2, n3, n4):
    v1 = n1 * 2 ** 0
    v2 = n2 * 2 ** 1
    v3 = n3 * 2 ** 2
    v4 = n4 * 2 ** 3
    r = v1 + v2 + v3 + v4
    return r


nBinario = int(input())
n1, n2, n3, n4 = sep(nBinario)
resultado = calc(n1, n2, n3, n4)
print(resultado)
