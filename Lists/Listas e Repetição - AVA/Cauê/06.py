par = []
impar = []

num = list(map(int,input().split(' ')))

for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(num)
print(par)
print(impar)
