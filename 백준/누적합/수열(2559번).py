n, m = map(int, input().split())
arr = list(map(int, input().split()))

add_num = []
add_num.append(sum(arr[:m]))
for i in range(n-m):
    add_num.append(add_num[i]-arr[i]+arr[i+m])
print(max(add_num))
