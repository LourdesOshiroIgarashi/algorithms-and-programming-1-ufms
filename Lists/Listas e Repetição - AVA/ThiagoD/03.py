def read():
    return float(input())
    

notas = []
    
for i in range(15):
    n = read()
    notas.append(n)
    
print(notas)
print(sum(notas) / len(notas))
