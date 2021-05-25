num = []
par = []
impar = []

for i in range(20):
    num.append(float(input()))

print(num)

for i in num:
    if i % 2 == 0:
        par.append(i)

    else:
        impar.append(i)

print(par)
print(impar)
