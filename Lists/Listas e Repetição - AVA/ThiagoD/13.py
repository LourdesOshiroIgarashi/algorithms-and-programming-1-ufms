k = int(input())

valores = []

for i in range(k):
    j = i + 1
    valor = 5 * (i) - j ** 2
    valores.append(valor)

print("Sequência:")
for i in valores:
    print(i, end=" ")
print("\n")
print(f"Para k = {k}, o valor do somatório é: {sum(valores)}")
