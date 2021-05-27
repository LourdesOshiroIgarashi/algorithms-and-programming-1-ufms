# Leia uma palavra e verifique se esta é palíndromo. Uma palavra é
# palíndromo se sua leitura nas ordens direta e inversa são iguais.
# Você deve implementar uma função para verificar se uma dada palavra
# ou frase é palíndromo.

def reverse(str):
    str = str[::-1]
    return str


palavra = input()
reverseString = reverse(palavra)

print(bool(palavra == reverseString))

# if bool(string == reverseString) == True:
#   print("Essa palavra é um palíndromo.")
# else:
#   print("essa palavra não é um palíndromo.")
