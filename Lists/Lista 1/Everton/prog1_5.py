valores = list(map(float, input().split()))

j = len(valores)
soma = 0
for i in valores: #SE DIGITAR 10 VALORES, O VALOR DE #I SERÁ 10
    soma = soma + i

print("A média dos {} valores digitados é {} ".format(j,soma/j))