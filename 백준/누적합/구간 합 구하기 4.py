n, m = map(int, input().split())
num_arr = []
num_arr = list(map(int, input().split()))
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split()))) 

sum_arr = [num_arr[0]]
for i in range(1, n):
    sum_arr.append(sum_arr[i-1] + num_arr[i])

for i in arr:
    if(i[0] == 1):
        print(sum_arr[i[1]-1])
        continue
    print(sum_arr[i[1]-1]-sum_arr[i[0]-2])
