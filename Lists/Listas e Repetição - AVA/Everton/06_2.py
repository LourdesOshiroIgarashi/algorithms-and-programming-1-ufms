inteiros = list(map(int, input().split()))

pares = [x for x in inteiros if x%2==0]
impar = [x for x in inteiros if x%2!=0]
print(f'''{inteiros}
      {pares}
      {impar}''')
