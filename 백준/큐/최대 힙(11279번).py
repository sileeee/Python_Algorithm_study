import sys
import heapq

n = int(input())
h = []

for _ in range(n):
    read = int(sys.stdin.readline().rstrip())
    if read != 0:
        heapq.heappush(h, (-read, read))
    elif read == 0 and len(h) != 0:
        print(heapq.heappop(h)[1]) 
    else:
        print(0)
