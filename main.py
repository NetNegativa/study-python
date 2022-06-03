n = int(input())
l = []

for i in range(n):
    s = input()
    l.append(s)

k = int(input())

for i in range(len(l)):
    s = l[i]
    print(s[k - 1:k], end='')