#DECLARANDO AS VARIÁVEIS
n = []
dado1 = 0
dado2 = 0
dado3 = 0
dado4 = 0
dado5 = 0
dado6 = 0
#ENTRADA DE DADOS
n = list(map(int, input("DIGITE AS OCORRÊNCIAS DAS FACES DE CADA JOGADA: ").split())) #A QUANTIDADE DE OCORRÊNCIA PODE SER QUALQUER UMA;

#PROCESSAMENTO
for i in range(len(n)):
    if n[i] == 1:
        dado1 = dado1 + 1
    elif n[i] == 2:
        dado2 = dado2 + 1
    elif n[i] == 3:
        dado3 += 1
    elif n[i] == 4:
        dado4 += 1
    elif n[i] == 5:
        dado5 += 1
    elif n[i] == 6:
        dado6 += 1

print('''A face 1 do dado ocorreu: {},
A face 2 do dado ocorreu: {},
A face 3 do dado ocorreu: {},
A face 4 do dado ocorreu: {},
A face 5 do dado ocorreu: {},
A face 6 do dado ocorreu: {},
'''.format(dado1, dado2, dado3, dado4, dado5, dado6))