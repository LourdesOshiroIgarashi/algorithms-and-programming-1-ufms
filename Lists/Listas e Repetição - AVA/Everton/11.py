x = float(input()) #valor
y = int(input()) #valor top
lista = []
soma = 0
for i in range(1, y+1, 1):
  var = i*x**i/i**2
  soma = soma + var
  lista.append(round(var, 3))

for j in range(0,len(lista),1):
  print('{:.3f}'.format(lista[j]), end=' ')

print("\n\nO valor do somatório é: {:.4f}".format(soma))
