#Entrada
lista = list(map(float,input("Digite 10 números reais: ").split(" ")))
#Processamento
for i in range(9, -1 , -1):
    print(lista[i], end = ' ')

