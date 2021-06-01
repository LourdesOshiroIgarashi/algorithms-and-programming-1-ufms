#DECLARAÇÃO DE VARIÁVEIS
media = []
maior = 0

#ENTRADA DAS NOTAS
for i in range(6):#0,1,2,3,4,5
  x = list(map(float, input().split()))
  media.append(sum(x)/len(x))


print('''Médias
Média do aluno 1: {}
Média do aluno 2: {}
Média do aluno 3: {}
Média do aluno 4: {}
Média do aluno 5: {}
Média do aluno 6: {}'''.format(round(media[0], 3), round(media[1], 3), round(media[2], 3), round(media[3], 3), round(media[4], 3), round(media[5], 3), ))

for i in media:
  if i >= 7:
    maior += 1
print(f'Existem {maior} alunos com média maior ou igual a 7.0')

