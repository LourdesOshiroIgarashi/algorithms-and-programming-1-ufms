'''Um jardineiro deseja saber se dados três números reais eles podem ser as medidas dos lados
de um triângulo. Caso os números formem um triângulo, o jardineiro deseja saber que tipo de triângulo
ele pode formar com os lados (equilátero, isósceles ou escaleno).
No caso de não formarem um triângulo, imprimir uma mensagem adequada. A entrada é dada por três números reais. '''


def semtriangulo():
    print("As medidas {:.2f}, {:.2f} e {:.2f} não formam um triângulo".format(a,b,c))
#ENTRADA DE DADOS
a = float(input())
b = float(input())
c = float(input())
#CONDIÇÃO DE EXISTÊNCIA
#x = a + b #a+b>c
#y = b + c #b+c>a
#z = a + c #a+c>b
#ENTÃO:
x = ((b-c)**2)**(1/2)

if x < a < b + c:
#CONDIÇAÕ DO TRIÂNGULO RETÂNGULO
#APLICAR O TEOREMA DE PITÁGORAS;
  if a**2 == b**2+c**2:
    tipo = 'retângulo'
  elif b**2 == c**2+a**2:
    tipo = 'retângulo'
  elif c**2 == a**2+b**a:
    tipo = 'retângulo'
#CONDIÇÃO DO TRIÂNGULO EQUILÁTERO:
  if a==b==c:
    tipo = 'equilátero'
  elif a==b or b==c or c==a:
    tipo = 'isóceles'
  else:
    tipo = 'escaleno'
  print("As medidas {:.2f}, {:.2f} e {:.2f} formam um triângulo {}".format(a,b,c,tipo))
else:
  semtriangulo()
