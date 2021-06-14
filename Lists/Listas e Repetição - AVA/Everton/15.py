n = int(input())
lista = []
lista1 = []
x = -1 
for i in range(n, 0, -1):
  lista.append(i)
for i in range(int(len(lista)/2)):
  var = lista[i]-lista[x]
  lista1.append(var)
  x = x -1
if lista[0] % 2 != 0:
    lista1.append(lista[int(len(lista)/2)])
print(lista)
print(lista1)
