from collections import deque

night = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
n = int(input())

for _ in range(n):
    map_size = int(input())
    visited = [[0] * map_size for _ in range(map_size)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited[sx][sy] += 1
    q = deque()
    q.append((sx,sy,0))

    while (q):
        tmp = q.popleft()
        x, y = tmp[0],tmp[1]

        if x == ex and y == ey:
            print(tmp[2])
            break
        
        for i in range(8):
            tx = night[i][0] + x
            ty = night[i][1] + y
            if 0 <= tx < map_size and 0 <= ty < map_size and visited[tx][ty]==0:
                visited[tx][ty] = 1
                q.append((tx,ty,tmp[2]+1))
