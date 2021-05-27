# Faça um programa que leia o número de matrícula do funcionário, o número
# de horas trabalhadas mensais, o valor que ele recebe por hora e o número
# de filhos e, em seguida calcule e escreva o salário deste funcionário,
# sendo que cada filho acrescenta 10% no salário do funcionário. Implemente
# uma função para leitura (que lê um único valor de entrada), uma para cálculo
# e outra para impressão dos resultados.

def leitura():
    x = input()
    return x


def calc(h, v, f):
    salario = h * v
    aumento = f * (salario * (10 / 100))
    salarioTotal = salario + aumento
    return salarioTotal


def Print(x):
    print(x)


matr = int(leitura())
horas = float(leitura())
valor = float(leitura())
filhos = int(leitura())

Print(calc(horas, valor, filhos))
