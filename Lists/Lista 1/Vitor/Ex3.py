#Entrada
lista = list(map(int,input("Digite 20 valores inteiros: ").split(" ")))
#Processamento
pares = []
impar = []
for i in lista:
    if i%2==0:
        pares.append(i)
    else:
        impar.append(i)
#Sáida
print("Pares: {} \nÍmpares: {} \nGeral: {}".format(pares,impar,lista))