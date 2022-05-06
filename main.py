n = int(input())
b = 0

for i in range(1, n + 1):
    if n % i == 0:
        b += i
print(b)