idades = list(map(int, input().split()))
alturas = list(map(float, input().split()))

alturasAcimaDe13 = []
for i in range(len(idades)):
    if idades[i] >= 13:
        alturasAcimaDe13.append(alturas[i])

if alturasAcimaDe13 != []:
    media = sum(alturasAcimaDe13) / len(alturasAcimaDe13)


anoes = 0

for i in range(len(idades)):
    if idades[i] >= 13 and alturas[i] < media:
        anoes += 1

if alturasAcimaDe13 == []:
    print("Idade || Altura")
    for i in range(len(idades)):
        print(f"{idades[i]:3d}{alturas[i]:11.2f}")
    print("\n")
    print("Não existem pessoas com 13 anos ou mais nesta amostra.")

else:
    print("Idade || Altura")
    for i in range(len(idades)):
        print(f"{idades[i]:3d}{alturas[i]:11.2f}")
    print("\n")
    print(f"Média de altura das pessoas com 13 anos ou mais: {media:.2f}")
    print(
        f"Existem {anoes} pessoas com 13 anos ou mais que estão abaixo da média das pessoas com esta faixa etária")
