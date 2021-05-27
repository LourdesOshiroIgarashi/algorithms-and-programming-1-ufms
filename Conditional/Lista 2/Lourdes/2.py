#  Sendo os valores de r, para o raio da bola,
#  a, b e c para as dimensoes de largura, profundidade e altura da caixa, respectivamente,
#  responda se a bola cabe ou nao na caixa em cada um dos casos

r, a, b, c = map(float, input().split(" "))

d = 2 * r

if d <= a and d <= b and d <= c:
    print("Cabe")
else:
    print("Não Cabe")
