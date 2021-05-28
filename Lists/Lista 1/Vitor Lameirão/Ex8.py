#Defininção de função
def soma(lista):
    soma = 0
    for a in lista:
        soma += a
    return soma
#Entrada e processamento
idades = []
alturas = []
for i in range(2):
    print("Digite a idade e altura da pessoa {}.".format(i+1))
    x = int(input("Idade: "))
    y = float(input("Altura: "))
    idades.append(x)
    alturas.append(y)

media_alt = soma(alturas)/2
c = 0 
for i in range(2):
    if idades[i] > 13 and media_alt > alturas[i]:
        c=+1

#Saída
print("{} pessoas com mais de 13 anos tem altura menor que a média.".format(c))