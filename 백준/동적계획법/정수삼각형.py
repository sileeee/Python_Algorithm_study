line = int(input())
arr = []

for i in range(line) :                            
    arr.append(list(map(int,input().split())))

for i in range(1, line):
    for j in range(i+1):
        if j==0:
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[line-1]))
