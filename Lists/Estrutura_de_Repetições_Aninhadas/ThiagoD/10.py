m, n = map(int, input().split())

for i in range(m + 1, n + 1):
    for j in range(i):
        if i % (j + 1) == 0 and ((j + 1) != 1 or (j + 1) != i):
            continue
        else:
            print(j, end=" ")
    print("")
