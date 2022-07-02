from sys import stdin

# input
n, m = map(int, input().split())
arr = [[0]* (n + 1)]
for _ in range(n):
    arr.append([0] + [int(x) for x in stdin.readline().split()])

# create sum map
for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]

# calculate the answer
for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])
