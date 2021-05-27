x, y, z = input().split()
x = int(x)
y = int(y)
if z == "+":
  soma = x + y
  print(x, z, y, "=", soma)
  
elif z == "-":
  subtracao = x - y
  print(x, z, y, "=", subtracao)

elif z == "*":
  multiplicacao = x * y
  print(x, z, y, "=", multiplicacao)

elif z == "/":
  divisao = x / y
  print(x, z, y, "=", divisao)
