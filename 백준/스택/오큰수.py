# 시간초과
n = int(input())
arr = list(map(int, input().split()))
s = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]<arr[j]:
            s.append(arr[j])
            break
        elif arr[i] >=arr[j] and j == len(arr)-1:
            s.append(-1)
s.append(-1)
for i in s:
    print(i, end=' ')
