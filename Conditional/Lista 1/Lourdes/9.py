x, y = map(int, input().split(" "))

if x == 0 and y == 0:
    print("origem")

elif x > 0 and y > 0:
    print("1 quadrante")

elif x < 0 and y > 0:
    print("2 quadrante")

elif x < 0 and y < 0:
    print("3 quadrante")

elif x > 0 and y < 0:
    print("4 quadrante")

elif x == 0 and y != 0:
    print("Eixo y")

elif x != 0 and y == 0:
    print("Eixo x")

else:
    print("ta errado")
