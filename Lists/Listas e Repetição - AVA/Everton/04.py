aux_in = 0
aux_su = 0

lista = list(map(float, input().split()))
media = sum(lista)/len(lista)

print("O valor médio da lista: ", end="")
for i in lista:
    print(i, end=" ")
print(' é: {:.6f}\n'.format(media))


for i in lista:
  if i > media:
    aux_su += 1
  else:
    aux_in += 1

print('Existem {} valores menores ou iguais a média e {} valores maiores que a média.'.format(aux_in, aux_su))
