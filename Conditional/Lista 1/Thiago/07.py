# Leia 2 valores numéricos e um símbolo correspondente a uma das operações.
# soma (+), subtração(-), divisão(/) e multiplicação(*)

n1, n2, op = input().split()
n1 = int(n1)
n2 = int(n2)

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    print(n1 / n2)
elif op == "*":
    print(n1 * n2)
else:
    print("Sua operação matemática não é válida.")
