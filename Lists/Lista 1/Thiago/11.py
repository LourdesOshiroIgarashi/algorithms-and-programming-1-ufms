x = int(input())
lista = [x]

for n in range(2, 100):
    y = (n * x ** n) / n ** 2
    lista.append(y)

media = sum(lista) / len(lista)

termosAbaixoDaMedia = 0

for i in lista:
    if i < media:
        termosAbaixoDaMedia += 1

print(f"Média = {media:.2f}")
print(f"Termos Abaixo da Média = {termosAbaixoDaMedia}")
