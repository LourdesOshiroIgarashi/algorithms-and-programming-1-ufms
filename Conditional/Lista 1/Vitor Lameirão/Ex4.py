#Entrada
x= float(input("Digite um número de no máximo duas casas decimais: "))
#Processamento
if len(x)==1 or (x[2]==0 and x[3]==0):
    print("O número {} é inteiro.".format(x))
else:
    print("O número {} é decimal.".format(x))