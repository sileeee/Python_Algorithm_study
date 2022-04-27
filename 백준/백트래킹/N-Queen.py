def is_promising(x):
    for i in range(x):
        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == abs(x - i):
            return False
    return True

def dfs(row):
    global count
    if(row == n):
        count+=1
        return
    for i in range(n):
        graph[row] = i # 3,3이면 -> (1,1)(2,2)체크 / (4,2) (5,1)
        if is_promising(row):
            dfs(row+1)
        
n = int(input())
count = 0
graph = [0]*n
dfs(0)
print(count)
