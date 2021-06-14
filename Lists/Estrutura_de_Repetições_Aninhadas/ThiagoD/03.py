x = int(input())
n = [1]

for i in range(x):
    for j in n:
        print(j, end=" ")
    print("")
    n.append(i + 2)
