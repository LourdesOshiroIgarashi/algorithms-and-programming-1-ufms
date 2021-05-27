# Leia 4 notas e, em seguida, apresente as notas lidas bem como a média das mesmas.

def listReader():
    lista = list(map(float, input().split()))
    return lista


# sum(lista):
# for item in lista:
#   soma = soma + item

lista = listReader()
somaDasNotas = sum(lista)
média = somaDasNotas / len(lista)
print(f"A média das notas é {média:.2f}")
