'''Considere o problema de computar o valor absoluto de um número real.
O valor absoluto de um número real x é dado por f(x) = x se x >= 0 ou f(x) = -x se x < 0.
Projete e implemente um programa em Python que lei um número de ponto flutuante x, calcule e imprima o valor absoluto de x.'''

x = float(input())

y = (x**2)**(1/2)

 
print("|{:.2f}| = {:.2f}".format(x,y))
