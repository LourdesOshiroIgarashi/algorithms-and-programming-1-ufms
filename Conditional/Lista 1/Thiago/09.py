# Programa recebe dois valores em uma única linha (x, y) e fala se o ponto formado por esses
# valores se encontra na origem, no eixo x, no eixo y, ou em um dos quadrantes e qual deles de um plano cartesiano.

def posicao(x, y):
    if x == 0 and y == 0:
        print("O ponto se encontra na origem.")
    elif x == 0 and y != 0:
        print("O ponto se encontra no eixo Y.")
    elif x != 0 and y == 0:
        print("O ponto se encontra no eixo X.")
    elif x > 0 and y > 0:
        print("O ponto se encontra no 1° quadrante.")
    elif x < 0 and y > 0:
        print("O ponto se encontra no 2° quadrante.")
    elif x < 0 and y < 0:
        print("O ponto se encontra no 3° quadrante.")
    elif x > 0 and y < 0:
        print("O ponto se encontra no 4° quadrante.")


x, y = map(int, input().split())

posicao(x, y)
