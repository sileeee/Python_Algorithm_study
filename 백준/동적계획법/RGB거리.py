import sys

house = int(input())
read = lambda: sys.stdin.readline().rstrip()
arr = []
sum = 0

for i in range(house):
    arr.append(list(map(int, read().split())))

for i in range(1, house):
    # R
    arr[i][0] = min(arr[i-1][1],arr[i-1][2])+arr[i][0]
    #G
    arr[i][1] = min(arr[i-1][0],arr[i-1][2])+arr[i][1]
    #B
    arr[i][2] = min(arr[i-1][0],arr[i-1][1])+arr[i][2]
print(min(arr[house-1]))ㅍ
