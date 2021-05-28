#Definindo funções
def Saida(a,b,c):
    if a==0:
        if b==0:
            print("O jogo durou {} segundos.".format(c))
        else: 
            print("O jodo durou {} minutos e {} segundos.".format(b,c))    
    else:
        print("O jogo durou {} horas, {} minutos e {} segundos.".format(a,b,c))

#Entrada
h1,m1,s1= map(int,input("Insira o horário inicial do jogo: ").split())
h2,m2,s2= map(int,input("Insira o horário final do jogo: ").split())
#Processamento
seg= s2-s1
min= m2-m1
hor= h2-h1

if s1>s2:
    seg=seg+60
    min=min-1
if m1>m2:
    min=min+60
    hor=hor-1
if h1>h2:
    hor=hor+24

Saida(hor,min,seg)
