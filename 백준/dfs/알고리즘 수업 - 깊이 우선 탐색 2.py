# error

def dfs(v, seq):
    visited[v] = seq
    seq +=1
    for i in arr[v]:
        if visited[i] == 0:
            dfs(i, seq)

seq = 1
n, m, r = map(int, input().split())
visited = [0]*(n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    arr[u].sort(reverse=True)
    arr[v].sort(reverse=True)

dfs(r, seq)
for i in range(n):
    print(visited[i+1])
