#Entrada
valores = list(map(float,input("Digite 10 valores numéricos: ").split(" ")))
#Processamento
soma = 0
for i in valores:
    soma = soma + i
media = soma/len(valores)
#Saída
print("Foram lidos {} números. \nA média desses números foi {}.".format(len(valores),media))