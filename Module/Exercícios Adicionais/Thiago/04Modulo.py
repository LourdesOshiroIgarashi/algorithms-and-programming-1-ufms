# Função que decompõe o número em 3 variáveis, uma para cada digito
def decomp(n):
    num2 = n % 10
    n2 = n // 10

    num1 = n2 % 10
    n1 = n2 // 10

    num0 = n1

    return num0, num1, num2


n = int(input())
num0, num1, num2 = decomp(n)

print(f"{num0} {num1} {num2}")
