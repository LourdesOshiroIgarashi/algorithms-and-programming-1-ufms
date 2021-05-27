#ENTRADA DE DADOS
A = int(input('DIGITE O VALOR DO PESO A: '))
B = int(input('DIGITE O VALOR DO PESO B: '))
C = int(input('DIGITE O VALOR DO PESO C: '))
D = int(input('DIGITE O VALOR DO PESO D: '))

#CONDIÇÕES

if A==B+C+D:
  if D==B+C:
    if B==C:
      print('Equilíbrio')
    else:
      print('Não está em equilíbrio')
  else:
    print('Não está em equilíbrio')
else:
  print('Não está em equilíbrio')


#PA = 8, PB = 4, PC = 2 e PD = 2
#Não está em Equilíbrio
#PA = 4, PB = 1, PC = 1 e PD = 2
#Está em Equilíbrio
