from collections import deque

n, m = map(int, input().split())
arr = list(map(int,input().split()))
q = deque()
sum = 0

for i in range(n):
    q.append(i+1)

for i in arr:
    mid = len(q)//2
    if q.index(i)<=mid:
        while(q[0] != i):
            sum += 1
            q.append(q.popleft())
        q.popleft()                
    else:
        while(q[0] != i):
            sum+=1
            q.appendleft(q.pop())
        q.popleft()
print(sum)
