s = []
for _ in range(int(input())):
    arr = input()
    for i in arr:
        if len(s)==0:
            s.append(i)
        elif s[-1]==i:
            s.append(i)
        elif s[-1]!=i and len(s)!=0 and s[-1]=='(':
            s.pop()
    if len(s)!=0:
        print("NO")
    else:
        print("YES")
    s = []
