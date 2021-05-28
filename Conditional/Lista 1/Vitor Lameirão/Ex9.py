#Entrada
x,y=map(int,input("Digite um ponto no plano cartesiano, separado por vírgula: ").split(","))

#Processamento
if x>0:
    if y>=0:
        print("Primeiro quadrante.")
    else:
        print("Quarto quadrante.")
else:
    if x<0:
        if y<=0:
            print("Terceiro quadrante.")
        else:
            print("Segundo quadrante.")
    else:
        print("Origem.")
