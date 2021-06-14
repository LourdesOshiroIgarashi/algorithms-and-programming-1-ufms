m, n = map(int, input().split())


n = [(m + 1)]
start = m + 2
while n[-1] != n:
    n.append(start)
    start += 1

for i in n:
    div = []
    j = 1
    while j != (i + 1):
        if i % j == 0:
            div.append(j)
        j += 1
    print(div)
