aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []
aluno6 = []
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
cont = 0


for i in range(3):
    aluno1.append(float(input("Adicione as 3 notas do aluno 1: ")))
    aluno2.append(float(input("Adicione as 3 notas do aluno 2: ")))
    aluno3.append(float(input("Adicione as 3 notas do aluno 3: ")))
    aluno4.append(float(input("Adicione as 3 notas do aluno 4: ")))
    aluno5.append(float(input("Adicione as 3 notas do aluno 5: ")))
    aluno6.append(float(input("Adicione as 3 notas do aluno 6: ")))

#print(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
for i in aluno1:
    soma1 = soma1 + i
for i in aluno2:
    soma2 = soma2 + i
for i in aluno3:
    soma3 = soma3 + i
for i in aluno4:
    soma4 = soma4 + i
for i in aluno5:
    soma5 = soma5 + i
for i in aluno6:
    soma6 = soma6 + i

media1 = soma1/3
media2 = soma2/3
media3 = soma3/3
media4 = soma4/3
media5 = soma5/3
media6 = soma6/3

if media1 >= 7:
    cont = cont + 1
if media2 >= 7:
    cont = cont + 1
if media3 >= 7:
    cont = cont + 1
if media4 >= 7:
    cont = cont + 1
if media5 >= 7:
    cont = cont + 1
if media6 >= 7:
    cont = cont + 1

print("pessoas q tiveram 7 ou mais", cont)
