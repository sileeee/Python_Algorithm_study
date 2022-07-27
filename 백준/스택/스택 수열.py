# error

n = int(input())
arr = [x+1 for x in range(n-1, -1, -1)]
answer = []
result = []
s = []
j = 0

for _ in range(n):
    answer.append(int(input()))

for i in answer:
        if len(s)!=0 and s[-1] == i:
            s.pop()
            result.append("-")
            continue
        while(True):
            if len(arr)!=0:
                j = arr.pop() 
            else: 
                break
            if i != j and i > j:
                s.append(j)
                result.append("+")
            elif i == j:
                s.append(j)
                result.append("+")
                s.pop()
                result.append("-")
                break
            elif i < j : 
                print("NO")
if len(s)!=0:
    print("NO")
else:
    for x in result:
        print(x)
