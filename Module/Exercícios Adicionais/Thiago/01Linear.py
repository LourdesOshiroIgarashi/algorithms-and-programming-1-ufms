# Leia um inteiro e determine quantos dias, meses e anos existem na quantidade de dias informado. Considere que o ano tem 365 dias e um mês tem 30 dias.

tempo = int(input())
dias = tempo
meses = tempo / 30
anos = tempo / 360

print(f"Existem {meses:.2f} meses ou {anos:.2f} anos em {dias} dias.")


# ***************************************************************************************************************** #
# ********** Recebe um valor em dias e calcula quantos anos, meses e dias são equivalentes a esse valor. ********** #
# ***************************************************************************************************************** #

# Calcula o número de anos com a quantidade de dias dada.
anoRelativo = tempo // 360
# Calcula o número de meses, com o resto dos dias não usado nos anos.
mesRelativo = tempo % 360 // 30
# Calcula o número de dias, com o que não foi usado para calcular os anos e meses.
diaRelativo = (tempo % 360) % 30

print(f"{tempo} dias é igual a {anoRelativo} anos, {mesRelativo} meses e {diaRelativo} dias.")
