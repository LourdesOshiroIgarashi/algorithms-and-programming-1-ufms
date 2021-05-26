serie = []
termos_menores_que_a_media = 0
entrada = int(input())
for i in range(0, 101):
  serie.append(i*entrada**i/i**i)


media = sum(serie)/100

for i in serie:
  if i < media:
    termos_menores_que_a_media += 1

print("Existem", termos_menores_que_a_media, "termos abaixo da média.")
