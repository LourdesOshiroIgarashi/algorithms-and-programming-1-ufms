x = float(input())

termos = []

for i in range(15):
    j = i + 1
    valor = j * (x ** j) / (j ** 2)
    termos.append(valor)

media = sum(termos) / len(termos)

abaixo = 0
for valor in termos:
    if valor < media:
        abaixo += 1

for i in termos:
    print(f"{i:.3f}", end=" ")
print("\n")
print(f"A média dos termos da sequência é de {media:.2f}")

if abaixo == 1:
    print(f"Existe 1 único termo na sequência cujo valor é abaixo da média")
elif abaixo == 0:
    print(f"Não existem termos na sequência cujo valor é abaixo da média")
else:
    print(f"Existem {abaixo} termos na sequência que estão abaixo da média")
