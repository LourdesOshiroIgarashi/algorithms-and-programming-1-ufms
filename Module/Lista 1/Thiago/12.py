# Leia os lados de um retângulo e determine sua área e perímetro. Implemente
# funções para cada entrada de dados, processamento e saída.

def entrada():
    return input()


def calc(b, h):
    a = b * h
    p = (2 * b) + (2 * h)
    return a, p


def saida(a):
    print(a)


b, h = map(float, entrada().split())

a, p = calc(b, h)

saida(a)
saida(p)
