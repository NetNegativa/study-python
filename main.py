n = int(input())
checkCount = 0
numbersList = []
search = ''
tagList = []
searchList = []

for i in range(n):
    number = input()
    numbersList.append(number)

k = int(input())
for j in range(k):
    search = input()
    tagList.append(search)

for m in range(len(numbersList)):
    for n in range(len(tagList)):
        if tagList[n].lower() in numbersList[m].lower():
            checkCount += 1
    if checkCount == k:
        searchList.append(numbersList[m])
    checkCount = 0

print(*searchList, sep='\n')


