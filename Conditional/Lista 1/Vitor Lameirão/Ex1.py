x,y= map(float,input("Digite dois valores numéricos: ").split())
if (x>y):
    print("{} é maior que {}.".format(x,y))
elif (y>x):
    print("{} é maior que {}.".format(y,x))
else:
    print("Os dois números são iguais.")
