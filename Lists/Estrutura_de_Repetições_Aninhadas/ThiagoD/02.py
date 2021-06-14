# Para  um  dado  inteiro  positivon,  imprima  um  figura  como  no  exerc ́ıcio  anterior,  sendo  que  a  primeiralinha da figura tem 1 *, a segunda linha tem 2 *,
# a terceira linha tem 3 * e assim at ́e a linhan, que dever ́acontern* .

x = int(input())

for i in range(x):
    for j in range(i + 1):
        print("*", end="")
    print("")
