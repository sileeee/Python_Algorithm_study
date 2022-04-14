import itertools

arr = []
n, m = map(int, input().split())
for i in range(1, n+1):
  arr.append(i)
npm = list(itertools.permutations(arr, m))
for i in npm:
  print(*i, sep=' ')
