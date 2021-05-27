#  O mobile na sala da Maria e composto de tres hastes exatamente como na figura abaixo.
# Para que ele esteja completamente equilibrado, com todas as hastes na horizontal, os pesos das
# quatro bolas A, B, C e D tem que satisfazer todas as seguintes tres condicoes:
# A = B + C + D
# B + C = D
# B = C

Pa, Pb, Pc, Pd = map(int, input().split(" "))

if Pa == Pb + Pc + Pd and Pb + Pc == Pd and Pb == Pc:
    print("Está em Equilíbrio")

else:
    print("Não está em Equilíbrio")
