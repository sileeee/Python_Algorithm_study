n = int(input())
arr = []
arr = list(map(int, input().split()))
arr.sort()
minimum = 1000000
sum = 0

for i in arr: #[3,1,4,3,2]
    sum += i*n
    n-=1
print(sum)
