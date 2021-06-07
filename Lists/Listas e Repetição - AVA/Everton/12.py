k = int(input())
lista = []
soma = 0
for i in range(1, k+1, 1):
  var = 3*i-2
  lista.append(var)
  soma = soma + var
print('Sequência:')
for i in range(0, len(lista), 1):
  print('{}'.format(lista[i]), end=' ')

print('\n')
print('Para k = {}, o valor do somatório é: {}'.format(k, soma))
