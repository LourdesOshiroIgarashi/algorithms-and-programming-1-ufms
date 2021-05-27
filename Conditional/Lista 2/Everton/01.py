p = int(input('PORTA P: 1 Para a porta na DIREITA, e 0 para a Porta na ESQUERDA: '))
r = int(input('PORTA Q: 1 Para a porta na DIREITA, e 0 para a Porta na ESQUERDA: '))

if p==0:
  print('A esfera vai para o caminho C')
else:
  if r==0:
    print('A esfera vai para o caminho B')
  else:
    print('A esfera vai para o caminho A')
