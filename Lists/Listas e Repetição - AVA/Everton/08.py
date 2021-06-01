#VARIÁVEIS
contador = 0 #somar as pessoas com 13 anos ou mais
soma = 0 #somar as alturas das pessoas com 13 anos ou mais
        
#ENTRADA DE DADOS
idade = list(map(int, input().split()))
altura = list(map(float, input().split()))

for i in range(0, len(idade), 1):
    if idade[i] >= 13:
        soma = soma + altura[i]
        contador = contador + 1

if contador !=0:
    media = soma / contador #media das altura das pessoas com 13 anos ou mais
#reset contador
contador = 0
for i in range(0, len(idade), 1):
    if idade[i] >= 13:
        if altura[i] <= media:
            contador = contador + 1

print("Idade || Altura")
for i in range(0,len(idade), 1):
    print('{:3d}'.format(idade[i]), end ='')
    print('{:11.2f}'.format(altura[i]))

print('\n')
if contador == 0:
    print("Não existem pessoas com 13 anos ou mais nesta amostra.")
else:
    print('''Média de altura das pessoas com 13 anos ou mais: {:.2f}
Existem {} pessoas com 13 anos ou mais que estão abaixo da média das pessoas com esta faixa etária'''.format(media, contador))
