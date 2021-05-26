s1 = []
s2 = []

s3 = []
s4 = []

for i in range(10):
    s1.append(int(input()))

for i in range(10):
    s2.append(int(input()))

for i in range(10):
    s3.append(s1[i])
    s3.append(s2[i])

for i in range(10):
    s4.append(s2[i])
    s4.append(s1[i])

#  print(s1)
#  print(s2)
print(s3)
print(s4)
