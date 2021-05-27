# Faça um prgrama que receba o valor de um depósito e o valor da taxa de juros,
# calcule e mostre o valor do rendimento e o valor total depois do rendimento.
# Implemente funções para leitura dos dados de entrada, processamento e saída.

def entrada():
    return input()


def calc(d, j):
    r = (j / 100 * d)
    rTotal = d + r
    return r, rTotal


def saida(a):
    print(a)


d, j = map(float, entrada().split())

rend, valorTotal = calc(d, j)

saida(rend)
saida(valorTotal)
