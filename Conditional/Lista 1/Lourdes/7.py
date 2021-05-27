a, b, c = input().split(" ")

a = int(a)
b = int(b)

if c == "*":
    multi = a * b
    print(multi)

elif c == "+":
    soma = a + b
    print(soma)

elif c == "-":
    sub = a - b
    print(sub)

elif c == "/":
    divi = a / b
    print(divi)

else:
    print("ta errado")
