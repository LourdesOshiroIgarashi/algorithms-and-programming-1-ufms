par = []
impar = []

lista = list(map(int, input().split(" ")))

for i in lista:
    if i % 2 == 0:
        par.append(i)    
    else:
        impar.append(i)

print(lista)
print(par)
print(impar)
