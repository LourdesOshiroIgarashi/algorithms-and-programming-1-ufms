n = [101]
start = 102
while n[-1] != 276:
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
