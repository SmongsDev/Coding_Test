import sys; input = sys.stdin.readline
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]* n for _ in range(m)]
    visited = [[False]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x][y] = 1

    def bug(i,j):
        visited[i][j] = True
        q = deque([(i,j)])
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    res = 0    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                bug(i,j)
                res += 1
    print(res)


## 

for _ in range(int(input())):
    m, n, k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[a][b] = 1
    
    def bug(x,y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if graph[x][y] == 0:
            return
        graph[x][y] = 0
        bug(x,y-1)
        bug(x-1,y)
        bug(x+1,y)
        bug(x,y+1)
        return
    res = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bug(i,j)
                res += 1
    print(res)