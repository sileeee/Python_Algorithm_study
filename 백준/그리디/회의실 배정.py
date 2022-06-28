n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x:(x[1],x[0]))

start = 0
end = 0
result = 0
for i in range(len(arr)):
    if end<=arr[i][0]:
        result += 1
        end = arr[i][1]
        
print(result)
