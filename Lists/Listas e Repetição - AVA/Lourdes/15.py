x = int(input())
todos = []
alguns = []

for i in range(x, 0, -1):
    todos.append(i)

l = len(todos)

if l % 2 != 0:
    for i in range(l-1, 0, -2):
        alguns.append(i)
    print(todos)
    alguns.append(todos[len(todos) // 2])
    print(alguns)
else:
    for i in range(l-1, 0, -2):
        alguns.append(i)
    print(todos)
    print(alguns)
