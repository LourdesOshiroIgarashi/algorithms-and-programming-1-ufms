#Entrada 
x,y,simb= input("Dígite dois valores e o símbolo da operação que deseja ser realizada: ").split()
#Processamento
x=int(x)
y=int(y)
if simb=="+":
    print("O resultado da soma entre {} e {} é {}.".format(x,y,x+y))
elif simb=="-":
    print("O resultado da subtração entre {} e {} é {}.".format(x,y,x-y))
elif simb=="*":
    print("O resultado da multiplicação entre {} e {} é {}.".format(x,y,x*y))
else:
    print("O resultado da divisão entre {} e {} é {}".format(x,y,x/y))