#1427

arr = []

for i in list(map(int, input())):
    arr.append(i)
arr.sort(reverse=True)
for i in arr:
    print(i, end='')
