# Leia a renda anual de um indivíduo e calcule o imposto que ele deve pagar com base na tabela.

renda = float(input())

imposto1 = 0
imposto2 = renda * (7.8 / 100)
imposto3 = renda * (15 / 100)
imposto4 = renda * (22.5 / 100)
imposto5 = renda * (27.5 / 100)

if renda <= 1434.59:
    print(f"Imposto = R${imposto1:.2f}")
elif 1434.60 <= renda <= 2150:
    print(f"Imposto = R${imposto2:.2f}")
elif 2150.01 <= renda <= 2866.70:
    print(f"Imposto = R${imposto3:.2f}")
elif 2866.71 <= renda <= 3582:
    print(f"Imposto = R${imposto4:.2f}")
else:
    print(f"Imposto = R${imposto5:.2f}")
