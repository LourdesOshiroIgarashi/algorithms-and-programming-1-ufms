def notas(troco):
    notas10 = troco // 10
    notas5 = (troco % 10) // 5
    moedas = ((troco % 10) % 5) // 1

    return notas10, notas5, moedas


preco, pagamento = map(int, input("Insira o preço do produto e o valor recebido como pagamento divididos por um espaço.\n").split())
troco = pagamento - preco

notasDez, notasCinco, moedasUm = notas(troco)

print(f"Preço = {preco} \nValor pago = {pagamento} \ntroco = {troco}")
print(f"Número de notas de 10 reais no troco = {notasDez} \nNúmero de notas de 5 reais no troco = {notasCinco} \nNúmero de moedas de 1 real no troco = {moedasUm}")
