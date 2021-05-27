# Leia dois valores, o primeiro correspondente ao valor de uma compra e outro correspondente ao valor pago pelo cliente.
# Determine a quantidade de notas de 10, 5 e de 1 real que devem compor o troco deste cliente. Assuma que os valores de entrada são inteiros.

#  Recebe os valores em uma única linha e os transforma em integers.
preco, pagamento = map(int, input("Insira o preço do produto e o valor recebido como pagamento divididos por um espaço.\n").split())

troco = pagamento - preco
notas10 = troco // 10
notas5 = (troco % 10) // 5
moedas = ((troco % 10) % 5) // 1

print(f"Preço = {preco} \nValor pago = {pagamento} \ntroco = {troco}")
print(f"Número de notas de 10 reais no troco = {notas10} \nNúmero de notas de 5 reais no troco = {notas5} \nNúmero de moedas de 1 real no troco = {moedas}")
