import itertools

arr = []
n, m = map(int, input().split())
for i in range(1, n+1):
  arr.append(i)
for i in itertools.combinations_with_replacement(arr, m):
    print(*i, sep=" ")
