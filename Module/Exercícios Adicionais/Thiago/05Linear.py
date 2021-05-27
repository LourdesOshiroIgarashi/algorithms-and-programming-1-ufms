# Leia um determinado valor inteiro correspondente à segundos. Determine quantas horas, minutos e segundos existem nesta quantidade de segundos informado.

valor = int(input())

h = valor // 3600
m = valor % 3600 // 60
s = valor % 3600 % 60

print(f"{valor} segundos equivale a {h}:{m}:{s}")
