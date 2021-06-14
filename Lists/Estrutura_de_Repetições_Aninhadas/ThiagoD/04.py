x = int(input())
n = [1]

for i in range(x):
    soma = 0
    for j in n:
        if j == n[-1]:
            print(j, end=" = ")
        else:
            print(j, end=" + ")
        soma += j
    print(f"{soma}")
    n.append(i + 2)
