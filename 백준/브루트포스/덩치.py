n = int(input())
x = [[0] * 2 for i in range(n)] # 2열5행

for i in range(n):
  a, b  = map(int, input().split())
  x[i][0] = a
  x[i][1] = b

for i in range(n):
  sum = 1
  for j in range(n):
    if(i == j):
      continue
    elif(x[i][0]<x[j][0] and x[i][1]<x[j][1]):
      sum +=1
  print(sum, end=' ')
