t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))
tri = [0 for _ in range(100)]
tri[0]=  1
tri[1]=  1
tri[2]=  1
tri[3]=  2
tri[4]=  2
for i in arr:
    for j in range(5, i):
        if (tri[j]):
            continue
        else:
            tri[j] = tri[j-1] + tri[j-5]
    print(tri[i-1])
