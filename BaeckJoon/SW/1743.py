import sys; input = sys.stdin.readline
from collections import deque
n,m,k = map(int,input().split())
directions = [(-1,0),(0,1),(1,0),(0,-1)]
visited = [[True] * (m+1) for _ in range(n+1)]
for i in range(k):
    a, b = map(int,input().split())
    visited[a][b] = False

def bfs(i,j):
    cnt = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 < nx <= n and 0 < ny <= m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt

result = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if not visited[i][j]:
            result = max(result, bfs(i,j))
print(result)