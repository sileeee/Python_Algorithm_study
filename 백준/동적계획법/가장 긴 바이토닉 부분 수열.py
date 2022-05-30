# error

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
    
# 증가하는 수열 up[][] , 감소하는 수열 down[][]
# 증가하면 up[시작 인덱스][현재 인덱스] += 1하면서 길이 누적, 그렇지 않으면 유지

up = [[0]*n for _ in range(n)]
down = [[0]*n for _ in range(n)]
length = []

for i in range(0, n-1):
    for j in range(1, n):
        if arr[i]<arr[j]:
            up[i][j] = up[i][j-1]+1
            down[i][j] = down[i][j]
        else:
            up[i][j] = up[j][j-1]
            down[i][j] = down[i][j-1]+1

# ...
         
