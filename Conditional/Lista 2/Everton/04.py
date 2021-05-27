a = int(input('NÚMERO DE ALUNOS: '))
m = int(input('NÚMERO DE MONITORES: '))

total = a + m

qtd_viagens = total // 50

if qtd_viagens%50 != 0:
  print('Serão necessárias {} viagens para que todos chegem ao topo'.format(qtd_viagens + 1))
else:
  print('Serão necessárias {} viagens para que todos chegem ao topo'.format(qtd_viagens))
