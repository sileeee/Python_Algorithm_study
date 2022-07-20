# error

from queue import PriorityQueue

q = PriorityQueue()
n = int(input())
arr = []

for _ in range(n):
    i = int(input())
    arr.append(i)
    if i<0:
        q.put((i*-0.9, i))
    elif i == 0:
        if q.empty():
            print("0")
        else:
            print(q.get()[1])
    else:
        q.put((i, i))
    

