firstNum = int(input())
secondNum = int(input())
checkSum = 0

for i in range(firstNum, secondNum + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            checkSum += 1
    if checkSum == 2:
        print(i)
    checkSum = 0