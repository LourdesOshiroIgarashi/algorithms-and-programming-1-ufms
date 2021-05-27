x = int(input("Digite um número de 1 a 12: "))

if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print("Mês de 31 dias.")
elif x == 4 or x == 6 or x == 9 or x == 1:
    print("Mês de 30 dias.")
elif x == 2:
    print("Mês de 28 ou 29 dias.")
else:
    print("Seu número não está entre 1 e 12.")
