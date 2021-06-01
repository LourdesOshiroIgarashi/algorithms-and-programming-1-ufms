#declarando a variável
lista = []
soma = 0
#entrada das notas
for i in range(0,15,1):
  nota = float(input())
  lista.append(nota)
for i in lista:
  soma = soma + i

media = soma / 15

print(lista)
print(media)
