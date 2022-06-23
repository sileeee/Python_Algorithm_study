n, k= map(int, input().split())
arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

for i in range(len(arr)-1, -1, -1):
    if k==0:
        break
    if arr[i]>k:
        continue
    result += int(k/arr[i])
    k%=arr[i]
print(result)
