# Leia um número inteiro de três dígitos e o decomponha. Exemplo:
# Entrada: 342
# Saída: 3 4 2

n = int(input())

# Seleciona o último digito do número dado.
num2 = n % 10
n2 = n // 10

# Seleciona o penúltimo número do número dado.
num1 = n2 % 10
n1 = n2 // 10

# Seleciona o primeiro número do número dado.
num0 = n1

print(f"{num0} {num1} {num2}")
