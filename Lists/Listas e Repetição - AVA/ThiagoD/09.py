# Código full ruim pq eu tava cansadão já qnd fiz esse

lancamentos = list(map(int, input().split()))

f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0

for i in lancamentos:
    if i == 1:
        f1 += 1
    elif i == 2:
        f2 += 1
    elif i == 3:
        f3 += 1
    elif i == 4:
        f4 += 1
    elif i == 5:
        f5 += 1
    else:
        f6 += 1
    
print(f"Lançamentos: {lancamentos}")
print(f"Número de ocorrências da face 1 = {f1}")
print(f"Número de ocorrências da face 2 = {f2}")
print(f"Número de ocorrências da face 3 = {f3}")
print(f"Número de ocorrências da face 4 = {f4}")
print(f"Número de ocorrências da face 5 = {f5}")
print(f"Número de ocorrências da face 6 = {f6}")
