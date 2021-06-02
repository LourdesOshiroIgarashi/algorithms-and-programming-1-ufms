k = int(input())

valores = []
dois = -2

for i in range(k):
    l = i + 1
    um = 3 * l
    total = (um + dois)
    valores.append(total)

print("Sequência:")
for i in valores:
    print(i, end=" ")
print("\n")
print(f"Para k = {k}, o valor do somatório é: {sum(valores)}")
