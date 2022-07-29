n = int(input())
num = 1
s = []
result = []
flag = False

for i in range(n):
    x = int(input())
    while num <= x:
        s.append(num)
        result.append("+")
        num += 1
    if s[-1] == x:
        s.pop()
        result.append("-")
    else:
        print("NO")
        flag = True
        break
if flag == False:
    for i in result:
        print(i)
