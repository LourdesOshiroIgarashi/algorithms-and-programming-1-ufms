#Entrada
seq_Um = list(map(float,input("Digite os 10 números da primeira seqûencia: ").split(" ")))
seq_Dois = list(map(float,input("Digite os 10 números da segunda seqûencia: ").split(" ")))

#Processamento
int_um = []
int_dois = []
for i in range(10):
        int_um.append(seq_Um[i])
        int_um.append(seq_Dois[i])
        int_dois.append(seq_Dois[i])
        int_dois.append(seq_Um[i])

#Saída
print("Sequência intercalada de 1 e 2: {}. \nSequência intercalada de 2 e 1: {}.".format(int_um,int_dois))

        