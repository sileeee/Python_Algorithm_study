n, m = map(int, input().split())
A = []
B = []
arr = []
result = [[] for _ in range(n)]

for _ in range(n):
    A.append(list(map(int,input().split())))
m, k = map(int, input().split())
for _ in range(m):
    B.append(list(map(int,input().split())))

for i in range(n):
    result = []
    for l in range(k):
        a = 0
        for j in range(m):
            a += A[i][j] * B[j][l]
        result.append(a)
    print(*result)
