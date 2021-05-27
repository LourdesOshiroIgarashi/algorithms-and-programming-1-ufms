# Leia dois valores inteiros a e b informados pelo usuário e escreva uma
# função que calcule e retorne os valores a + b, a * b e a / b. A impressão
# dos resultados deve ser feita por uma função que recebe como entrada
# um único parâmetro correspondente ao valor a ser impresso.

def calc(a, b):
    soma = a + b
    mult = a * b
    div = a / b

    return soma, mult, div


def tela(a):
    print(a)


a = int(input())
b = int(input())

calc = calc(a, b)

tela(calc)
