n = int(input())
numbersList = []
searchList = []

for i in range(n):
    number = input()
    numbersList.append(number)

search = input()

for j in range(len(numbersList)):
    if search.lower() in numbersList[j].lower():
        searchList.append(numbersList[j])

print(*searchList, sep='\n')