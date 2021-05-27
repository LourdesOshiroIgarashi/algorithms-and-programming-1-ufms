# Leia dois valores correspondentes à horas (no formato horas:minutos:segundos) e mostre a soma destas horas.

h1, min1, s1 = map(int, input().split())
h2, min2, s2 = map(int, input().split())

somaS = (s1 + s2) % 60
valorPraMin = (s1 + s2) // 60

somaMin = ((min1 + min2) + valorPraMin) % 60
valorPraH = ((min1 + min2) + valorPraMin) // 60

somaH = (h1 + h2) + valorPraH

print(f"Valor 1 = {h1}:{min1}:{s1}")
print(f"Valor 2 = {h2}:{min2}:{s2}")
print(f"Soma = {somaH}:{somaMin}:{somaS}")
