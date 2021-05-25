#FUNÇÕES
def soma(x):
    soma = 0
    media = 0
    cont = 0
    for i in x:
        soma = soma + i
        media = soma / len(x)
    if media >= 7:
        cont = cont + 1
        return cont
    else:
        return cont
#DECLARANDO AS VARIÁVEIS NECESSÁRIAS
aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []
aluno6 = []

#ENTRADA DE DADOS
for i in range(1):
    aluno1 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 1: ').split()))
    aluno2 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 2: ').split()))
    aluno3 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 3: ').split()))
    aluno4 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 4: ').split()))
    aluno5 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 5: ').split()))
    aluno6 = list(map(float, input('DIGITE AS 3 NOTAS DO ALUNO 6: ').split()))

#CALCULANDO A MÉDIA DE CADA ALUNO
contagem = soma(aluno1) + soma(aluno2) + soma(aluno3) + soma(aluno4) + soma(aluno5) + soma(aluno6)

#SAÍDA FINAL
print(f'{contagem} alunos conseguiram nota acima ou igual a 7.')