numeros = []
impar = []
par = []
a = 0
for i in range(20):
  numeros.append(int(input()))


for i in numeros:
  if numeros[a]%2 == 0:
    par.append(numeros[a])
  else:
    impar.append(numeros[a])
  a = a + 1

print(numeros)
print(par)
print(impar)