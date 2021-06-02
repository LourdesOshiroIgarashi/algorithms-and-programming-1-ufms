x = float(input())
j = int(input())

soma = 0
valores = []

for i in range(j):
    an = (i + 1) * x ** (i + 1) / (i + 1) ** 2
    valores.append(f"{an:.3f}")
    soma += an

for i in valores:
	i = float(i)

for i in valores:
    print(i, end=" ")
print("\n")
print(f"O valor do somatório é: {soma:.4f}")
