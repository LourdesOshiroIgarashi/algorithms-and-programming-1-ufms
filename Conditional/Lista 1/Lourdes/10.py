x0, y0 = map(int, input().split(" "))
x1, y1 = map(int, input().split(" "))

a0, b0 = map(int, input().split(" "))
a1, b1 = map(int,input().split(" "))

if (x0 <= a0 <= x1 or x0 <= a1 <= x1) and (y0 <= b0 <= y1 or y0 <= b1 <= y1):
    print("Intercepta")

else:
    print("Não intercepta")
