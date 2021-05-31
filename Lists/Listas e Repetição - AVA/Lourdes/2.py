x = []

x = list(map(int, input().split(" ")))

for i in x:
    print(i, end=" ")

print("\n")
x.reverse()

for i in x:
    print(i, end= " ")
