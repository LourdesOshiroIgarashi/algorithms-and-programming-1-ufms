A, M = map(int, input().split(" "))

if A + M <= 50:
    print("Todos subirão juntos!")

else:
    viagens = (A + M) // 50
    if (A + M) % 50 != 0:
        viagens = viagens + 1
        print("Serão necessárias {} viagens para que todos cheguem ao topo".format(viagens))

    else:
        print("Serão necessárias {} viagens para que todos cheguem ao topo".format(viagens))
