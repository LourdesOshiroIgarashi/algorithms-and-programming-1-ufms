a = float(input())
b = float(input())
c = float(input())
r = float(input())

r = 2*r

if a >= r:
  print('CABE em A')
  if b >= r:
    print('CABE em B')
  else:
      print('FALHOU O TAMANHO DE B')
  if c >= r:
    print('CABE em C')
  else:
    print('FALHOU O TAMANHO DE C')
else:
  print('FALHOU O TAMANHO DE A')
