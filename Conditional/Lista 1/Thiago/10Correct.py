# recebe as coordenadas do primeiro ponto do retângulo em uma linha separadas por espaço, e as do 2 ponto da mesma maneira na próxima linha
def coordenadas():
    x1, y1 = map(int, input(
        "Insira os valores x e y da primeira coordenada (separados por espaço): ").split())
    x2, y2 = map(int, input(
        "Insira os valores x e y da segunda coordenada (separados por espaço): ").split())
    return x1, y1, x2, y2


# Coordenadas retnângulo 1 (r1)
r1x1, r1y1, r1x2, r1y2 = coordenadas()
# Coordenadas retângulo 2 (r2)
r2x1, r2y1, r2x2, r2y2 = coordenadas()

# Vê se os retângulos estão distantes um do outro no eixo x e y
if r1x1 > r2x2 or r1x2 < r2x1 or r1y1 > r2y2 or r1y2 < r2y1:
    print("Não há colisão.")
else:
    print("Há colisão.")
