a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 + b1 + a2 + b2) % 2 == 0:
    print('NO')
else:
    if (abs(a1 - a2) == 1 and abs(b1 - b2) == 2) or (abs(a1 - a2) == 2 and abs(b1 - b2) == 1):
        print('YES')
    else:
        print('NO')