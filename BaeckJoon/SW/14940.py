from collections import deque

n, m = map(int, input().split())
map = [ list(map(int, input().split())) for _ in range(n) ]
result = [[-1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

directions = [(-1,0),(0,1),(1,0),(0,-1)]

q = deque()
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            q.append((i,j,0))
            result[i][j] = 0
            visited[i][j] = True
        elif map[i][j] == 0:
            result[i][j] = 0
            visited[i][j] = True

while q:
    x, y, cost = q.popleft()

    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            q.append((nx,ny,cost+1))
            result[nx][ny] = cost+1
            visited[nx][ny] = True
            
for i in range(n):
    print(*result[i])