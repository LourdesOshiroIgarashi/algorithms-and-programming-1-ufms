# Leia 3 notas de um grupo de 6 alunos. Calcule e armazene a média de cada aluno e, em seguida, determine quantos alunos possuem média maior ou igual a 7.0.

# Lê uma série de números reais digitados na mesma linha e os transforma em uma lista.
def leitorLista():
    lista = list(map(float, input().split()))
    return lista


# Calcula a média dos valores da lista.
def calculadoraMedia(lista):
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)
    return media


# Recebe uma lista com as notas dos alunos 6 vezes (6 alunos) e as armazena dentro da lista notasAlunos.
notasAlunos = [leitorLista() for i in range(6)]

mediaAlunos = []

# Calcula a média das notas dos alunos e armazena essa média na lista mediaAlunos
for notas in notasAlunos:
    media = calculadoraMedia(notas)
    media = "{:.2f}".format(media)
    media = float(media)
    mediaAlunos.append(media)

alunosPassados = 0

# Calcula a quantidade de alunos que passaram de ano (obtiveram a nota mínima exigida).
for media in mediaAlunos:
    if media >= 7.0:
        alunosPassados += 1

print(f"Notas dos alunos = {notasAlunos}")
print(f"Média das notas de cada aluno = {mediaAlunos}")
print(
    f"Quantidade de alunos que possuem média maior ou igual a 7.0 = {alunosPassados}")
