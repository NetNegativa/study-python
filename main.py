num = int(input())

for i in range(num // 2 + 1):
    for j in range(i):
        print('*', end='')
    print()
for k in range(num // 2 + 1, 0, -1):
    for m in range(k):
        print('*', end='')
    print()