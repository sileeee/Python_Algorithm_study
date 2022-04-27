import itertools

arr = []
n, m = map(int, input().split())
for i in range(1, n+1):
  arr.append(i)
for i in itertools.product(arr, repeat=m):
    print(*i, sep=" ")
