# error

def dfs(row):
    global count
    if(row == n):
        count+=1
        return
    for i in range(n):
        graph[row] = i # 3,3 -> (1,1)(2,2) // (4,2) (5,1)
        for j in range(row):
            if(abs(graph[row]-graph[j]) == abs(row-j) or graph[row]==graph[j]):
                return
    dfs(row+1)

n = int(input())
count = 0
graph = [0]*n
dfs(0)
print(count)
