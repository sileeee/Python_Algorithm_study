N = int(input())
length = 0

tmp = N
while(tmp>0): # N의 자릿수를 구한다
  tmp //= 10
  length +=1

for i in range(1, N+1):
  result = i
  tmp = i
  while(tmp>0):
    result += tmp%10
    tmp //= 10
  if(result == N):
    print(i)
    break
  if(i == N):
    print(0)
