#DECLARAÇÃO DE VARIÁVEIS
pares = []
impar = []

#ENTRADA DOS VALORES
numeros = list(map(int, input().split()))

for i in numeros:
  if i%2 == 0:
    pares.append(i)
  else:
    impar.append(i)

print(numeros)
print(pares)
print(impar)
