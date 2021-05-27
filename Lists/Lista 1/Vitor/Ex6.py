#Entrada e Processamento
media = []
for i in range(6):
    print("Digite as notas do aluno {}:".format(i+1))
    soma_Notas = 0
    for i in range(3):
        soma_Notas += float(input("Nota {}: ".format(i+1)))
    media.append(soma_Notas/3)

c=0
for aprovado in media:
    if aprovado>=7:
        c = c+1

#Saída
print("A quantidade de alunos aprovados foi {}.".format(c))   