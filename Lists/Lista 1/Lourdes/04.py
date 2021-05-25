num = []
soma = 0

for i in range(11):
    num.append(int(input()))

n = len(num)

for i in num:
    soma = soma + i

media = soma / n
print(media)
