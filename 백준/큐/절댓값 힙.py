import sys
import heapq

n = int(input())
h = []

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    if i!=0:
        heapq.heappush(h, (abs(i), i))
    else:
        try:
            print(heapq.heappop(h)[1])
        except:
            print(0)
