#Definindo função
def Saida(renda,a):
    print("Você pagará {} reais de imposto".format(renda*a))

renda=float(input("Digite seu salário: "))

if renda<=2860.7:
    if renda>=2150.01:
        Saida(renda,0.15)
    else:
        if renda>=1434.60:
            Saida(renda,0.078)
        else:
            print("Isento de impostos.")    
else:
    if renda<=3582:
        Saida(renda,0.225)
    else:
        Saida(renda,0.275)            
