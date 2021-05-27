def tempoFixo(t):
    dias = t
    meses = t / 30
    anos = t / 365
    return dias, meses, anos


def tempoRelativo(tempo):
    # Calcula o número de anos com a quantidade de dias dada.
    anoRelativo = tempo // 365
    # Calcula o número de meses, com o resto dos dias não usado nos anos.
    mesRelativo = tempo % 365 // 30
    # Calcula o número de dias, com o que não foi usado para calcular os anos e meses.
    diaRelativo = (tempo % 365) % 30
    return anoRelativo, mesRelativo, diaRelativo


tempoEmDias = int(input())

dias, meses, anos = tempoFixo(tempoEmDias)
anoRelativo, mesRelativo, diaRelativo = tempoRelativo(tempoEmDias)

print(f"Existem {meses:.2f} meses ou {anos:.2f} anos em {dias} dias.")
print(f"{tempoEmDias} dias é igual a {anoRelativo} anos, {mesRelativo} meses e {diaRelativo} dias.")
