from collections import deque

n = int(input())
oper = []
d = deque()
for _ in range(n):
    oper.append(input())

for i in oper:
    if len(i)>10:
        op, num = i.split()
        if op == 'push_back':
            d.append(num)
        else:
            d.appendleft(num)
    else:
        if i == 'pop_front':
            if len(d) == 0:
                print('-1')
            else:
                print(d.popleft())
        elif i == 'pop_back':
            if len(d) == 0:
                print('-1')
            else:
                print(d.pop())
        elif i == 'size':
            print(len(d))
        elif i == 'empty':
            if len(d) == 0 :
                print('1')
            else:
                print('0')
        elif i == 'front':
            if len(d) == 0:
                print('-1')
            else:
                tmp = d.popleft()
                print(tmp)
                d.appendleft(tmp)
        elif i == 'back':
            if len(d) == 0:
                print('-1')
            else:
                tmp = d.pop()
                print(tmp)
                d.append(tmp)
    
