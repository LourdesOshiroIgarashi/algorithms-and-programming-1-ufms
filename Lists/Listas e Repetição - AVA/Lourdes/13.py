k = int(input())
soma = 0
somatorio = []

for i in range(1, k+1):
    formula = (5 * i) - 5 - i ** 2
    somatorio.append(formula)
    soma = soma + formula

print("Sequência:")

for i in somatorio:
    print(i, end=" ")
print(f"\n\nPara k = {k}, o valor do somatório é: {soma}")
