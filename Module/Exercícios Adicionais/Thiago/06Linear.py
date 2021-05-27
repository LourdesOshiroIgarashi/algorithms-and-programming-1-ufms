# Leia um número binário de 4 bits e determine o inteiro correspondente.

binario = int(input())
num = binario

n1 = binario % 10
num = binario // 10

n2 = num % 10
num = num // 10

n3 = num % 10
num = num // 10

n4 = num % 10

valor1 = n1 * 2 ** 0
valor2 = n2 * 2 ** 1
valor3 = n3 * 2 ** 2
valor4 = n4 * 2 ** 3

resultado = valor1 + valor2 + valor3 + valor4

print(resultado)
