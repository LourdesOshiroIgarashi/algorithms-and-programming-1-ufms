jogadas = list(map(int,input().split()))
faces = [0, 0, 0, 0, 0, 0]

for i in jogadas:
    faces[i-1] += 1

print("Lançamentos: {}".format(jogadas))
print("Número de ocorrências da face 1 = {}".format(faces[0]))
print("Número de ocorrências da face 2 = {}".format(faces[1]))
print("Número de ocorrências da face 3 = {}".format(faces[2]))
print("Número de ocorrências da face 4 = {}".format(faces[3]))
print("Número de ocorrências da face 5 = {}".format(faces[4]))
print("Número de ocorrências da face 6 = {}".format(faces[5]))
