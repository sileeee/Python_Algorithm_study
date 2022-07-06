# 시간 초과

n, m = map(int, input().split())
arr = list(map(int,input().split()))

arr2 = []
for i in arr:
    arr2.append(i%m)

sum_tmp = 0
result = 0
for i in range(n): 
    for j in range(i, n):
        sum_tmp += arr2[j]
        if(sum_tmp % 3 == 0):
            result += 1
    sum_tmp = 0
print(result)
