a = []
b = []
c = []
for i in range(5):
    a.append(int(input()))
    b.append(int(input()))
    c = a[:] + b[:]

print(c)