'''Dados dois números inteiros, num1 e num2, dizemos que num1 é um divisor de num2 se num2 % num1 == 0.
Projete e implemente um programa em Python que leia dois números inteiros, num1 e num2, e se num1 for divisor
de num2 imprima o resultado da divisão de acordo com o formato especificado, caso contrário imprima que num1 não é um divisor de num2.'''

num1 = int(input())
num2 = int(input())

if num2%num1 == 0:
    print(f'{num1} é divisor de {num2}')
else:
    print(f'{num1} não é divisor de {num2}')
