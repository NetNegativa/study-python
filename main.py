a = len(input())
b = len(input())
c = len(input())

if (2 * a - b - c) * (2 * b - c - a) * (2 * c - b - a) == 0:
    print('YES')
else:
    print('NO')
