# Recebe o horário em h m s divididos apenas por espaço.
def entrada():
    h, m, s = map(int, input(
        "Insira o horário separado apenas por espaço: ").split())
    return h, m, s


# Calcula a diferença entre os horários de começo e fim.
def calculo(h1, m1, s1, h2, m2, s2):
    s = s2 - s1
    m = m2 - m1
    h = h2 - h1
    return h, m, s


h1, m1, s1 = entrada()
h2, m2, s2 = entrada()

if s1 > s2:
    s2 = s2 + 60
    m2 = m2 - 1
if m1 > m2:
    m2 = m2 + 60
    h2 = h2 - 1
if h1 > h2:
    h2 = h2 + 24

hFinal, mFinal, sFinal = calculo(h1, m1, s1, h2, m2, s2)
print(f"O jogo durou: {hFinal} {mFinal} {sFinal}")
