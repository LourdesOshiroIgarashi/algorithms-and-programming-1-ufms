#DECLARAÇÃO DE VARIÁVEIS
dado1 = dado2 = dado3 = dado4 = dado5 = dado6 = 0
#ENTRADA DE DADOS
lancamentos = list(map(int, input().split()))

for i in range(0, len(lancamentos), 1):
    if lancamentos[i]==1:
        dado1 = dado1 + 1
    elif lancamentos[i]==2:
        dado2 += 1
    elif lancamentos[i]==3:
        dado3 += 1
    elif lancamentos[i]==4:
        dado4 += 1
    elif lancamentos[i]==5:
        dado5 += 1
    elif lancamentos[i]==6:
        dado6 += 1

print(f'''Lançamentos: {lancamentos}
Número de ocorrências da face 1 = {dado1}
Número de ocorrências da face 2 = {dado2}
Número de ocorrências da face 3 = {dado3}
Número de ocorrências da face 4 = {dado4}
Número de ocorrências da face 5 = {dado5}
Número de ocorrências da face 6 = {dado6}''')
