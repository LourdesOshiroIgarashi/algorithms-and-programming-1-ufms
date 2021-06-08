k = int(input())
somatorio = []
soma = 0

for i in range(1, k+1):
    formula = 3 * i - 2
    somatorio.append(formula)
    soma = soma + formula

print("Sequência:")

for i in somatorio:
    print(f"{i}", end=" ")

print("\n")
print(f"Para k = {k}, o valor do somatório é: {soma}")
