#FUNÇÃO
def cal(x):
  segundos = x % 60
  minutos = segundos_tt // 60
  horas = minutos // 60
  minutos = minutos %60
  print(horas, minutos, segundos)
#CORPO PRINCIPAL
#ENTRADA
horas_inicial, minutos_inicial, segundos_inicial = map(int, input().split())
horas_jg,      minutos_jg,      segundos_jg      = map(int, input().split())
#CALCULO DE SEGUNDOS TOTAIS
total_inicial = horas_inicial*60*60 + minutos_inicial*60 + segundos_inicial
total_jg_24 = horas_jg*60*60 + minutos_jg*60 + segundos_jg + 24*60*60
total_jg = horas_jg*60*60 + minutos_jg*60 + segundos_jg
#CONDIÇÕES
if horas_inicial > horas_jg:
  segundos_tt = total_jg_24 - total_inicial
  cal(segundos_tt)
else:
  segundos_tt = total_jg - total_inicial 
  cal(segundos_tt)
