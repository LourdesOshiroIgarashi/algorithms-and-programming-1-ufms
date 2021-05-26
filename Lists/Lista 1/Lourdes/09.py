n = int(input())

jogadas = []
faces = [0, 0, 0, 0, 0, 0]

for i in range(n):
    jogadas.append(int(input()))

for i in jogadas:
    faces[i-1] += 1

print(faces)
