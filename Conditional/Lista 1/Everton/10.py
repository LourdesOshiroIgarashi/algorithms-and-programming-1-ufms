#ENTRADA DE DADOS

#Primeiro retângulo
x1, y1 = map(int, input('Digite as coordenadas x1 e y1: ').split())
x2, y2 = map(int, input('Digite as coordenadas x2 e y2: ').split())
#Segundo retângulo
x3, y3 = map(int, input('Digite as coordenadas x3 e y3: ').split())
x4, y4 = map(int, input('Digite as coordenadas x4 e y4: ').split())


if y3>y2 or y4<y1 or x3>x2 or x1>x4:
  print('Não colidem')
else:
  print('Colidem')
