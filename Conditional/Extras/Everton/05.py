'''A Associação dos Programadores Independentes (API) faz uma reunião anual para discussão das políticas da associação.
Cada sede local da API envia um representante oficial para a reunião. A organização do evento oferece uma ajuda de custo
aos delegados baseado na distância da sede local ao local do evento de acordo com a tabela abaixo:

 

Distância Ida-e-Volta	Taxa
Até 500 quilômetros	R$ 0.15 por quilômetro
501 a 1000 quilômetros	R$ 75.00 + R$ 0.12 por cada quilômetro acima de 500
1001 a 1500 quilômetros	R$ 135.00 + R$ 0.10 por cada quilômetro acima de 1000
1501 a 2000 quilômetros	R$ 185.00 + R$ 0.08 por cada quilômetro acima de 1500
2001 a 3000 quilômetros	R$ 225.00 + R$ 0.06 por cada quilômetro acima de 2000
3001 ou mais quilômetros	R$ 285.00 + R$ 0.05 por cada quilômetro acima de 3000
 

Escreva um programa que leia o número da sede de um delegado e a distância de sua sede ao local do evento.
O programa deve computar e imprimir o valor da ajuda de custo de custo do delegado, de acordo com o formato abaixo.
A entrada dada por um inteiro representando o número da sede do representante e um inteiro representando a distância
em quilômetros da sede local do delegado ao local do evento.
A saída consiste em imprimir para o delegado (com mensagens apropriadas), o número da sede e o valor da ajuda de custo.'''

sede = int(input())
distancia_evento = int(input())

x = distancia_evento
if distancia_evento<501:
  valor = x*0.15
elif 501<=distancia_evento<=1000:
  valor = 75 + (x-500)*0.12
elif 1001<=distancia_evento<=1500:
  valor = 135 + (x-1000)*0.10
elif 1501<=distancia_evento<=2000:
  valor = 185 + (x-1500)*0.08
elif 2001<=distancia_evento<=3000:
  valor = 225 + (x-2000)*0.06
elif distancia_evento>=3001:
  valor = 285 + (x-3000)*0.05

print('Sede: {} - valor: R${:.2f}'.format(sede, valor))
