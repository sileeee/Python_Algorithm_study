n = int(input())

arr = list(map(int,input().split()))
arr_reverse = arr[::-1]

# arr : 1 5 2 1 4 3 4 5 2 1

# (가질 수 있는 길이의 최대값)
# up  : 1 2 2 1 3 3 4 5 2 1
# down: 1 2 3 3 3 4 1 2 5 1

up = [1 for i in range(n)]
down = [1 for i in range(n)]
max_length = 0

for i in range(n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            up[i] = max(up[i], up[j]+1)
        if arr_reverse[j]<arr_reverse[i]:
            down[i] = max(down[i], down[j]+1)
        
for i in range(n):
        max_length = max(max_length, up[i]+down[n-i-1])
print(max_length-1)
