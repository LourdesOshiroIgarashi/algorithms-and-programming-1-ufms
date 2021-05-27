# P = 0 e R = 0 -- C | P = 0 e R = 1 -- C
# P = 1 e R = 0 -- B | P = 1 e R = 1 -- A

p, r = map(int, input().split())

if p == 0:
    print("C")
elif r == 0:
    print("B")
else:
    print("A")
