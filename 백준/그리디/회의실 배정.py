# error

n = int(input())
increase = [1 for _ in range(n)]
arr = []
line = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in range(1, n):
    for j in range(i):
        if arr[j][1]<=arr[i][1] and arr[j][1]<=arr[i][0]:
            increase[i] = max(increase[i], increase[j]+1)
print(n-max(increase))
