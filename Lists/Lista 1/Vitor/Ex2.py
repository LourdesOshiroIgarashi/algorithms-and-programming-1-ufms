#Entrada
notas = list(map(float,input("Digite suas quatro notas: ").split(" ")))
#Processamento
soma = 0 
for i in notas:
    soma = soma + i
media = soma/len(notas)
#Saída
print("Notas: {} \nMédia: {}".format(notas,media)) 