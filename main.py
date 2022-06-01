n = int(input())
s = input()

for i in range(len(s)):
    d = ord(s[i]) - n
    if d < 97:
        d += 26
    print(chr(d), end='')
