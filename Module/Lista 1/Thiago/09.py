# Determine o calor das cariáveis n1 e n2 após a execução do código a seguir:

def leInteiro():
    return int(input("Digite um valor inteiro:"))


def Soma(n1, n2):
    soma = n1 + n2
    n1 = 2 * n1
    n2 = 2 * n2
    return soma


n1 = leInteiro()
n2 = leInteiro()

soma = Soma(n1, n2)

print("a soma de %d + %d é %d" % (n1, n2, soma))

# n1 = valor passado em leInteiro() e n2 também, pois seus novos valores só existem dentro da função Soma().
