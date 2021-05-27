'''Projete e implemente um programa em Python para ler os coeficientes, a, b e c, onde a ≠ 0, 
de uma equação do segundo grau e calcule as raízes da equação. A entrada é dada por 3 números (podem ser to tipo double).
A saída consiste em imprimir as raízes da equação com duas casas decimais ou uma mensagem
indicando que a equação não possui raízes reais. Para calcular a raiz quadrada, utilize a função math.sqrt(num) do módulo math.'''

import math
a, b, c = map(int, input().split())


delta = b**2 - 4*a*c
if delta>0:
    y1 = (- b + math.sqrt(delta))/2a
    y2 = (- b - math.sqrt(delta))/2a
    print('A equação possui as raízes {:.2f} e {:.2f}'.format(y2, y1))
elif delta == 0:
    y = (- b + math.sqrt(delta))/2a
    print('A equação possui uma única raiz: {:.2f}'.format(y))
    
else:
    print('A equação não possui raízes reais')
