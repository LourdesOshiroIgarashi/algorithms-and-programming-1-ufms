def read():
    x = int(input())
    return x


a = read()
b = read()
c = read()
d = read()

if b == c and b + c == d and b + c + d == a:
    print("S")
else:
    print("N")
