#DECLARAÇÃO DE VARIÁVEIS
intercalacao = []

numeros1 = list(input().split())
numeros2 = list(input().split())

t=0
c=0
while t<10:
  intercalacao.append(numeros1[t])
  intercalacao.append(numeros2[c])
  t = t + 1
  c = c + 1
print('Sequência 1:', numeros1)
print('Sequência 2:', numeros2)
print('Itercalação da Sequência 1 e Sequência 2: ')
print(intercalacao)
