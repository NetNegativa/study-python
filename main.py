n = int(input())
b = 0

for i in range(n + 1):
    if i % 2 == 0:
        b -= i
    else:
        b += i
print(b)