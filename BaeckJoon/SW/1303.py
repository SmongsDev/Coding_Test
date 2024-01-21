import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
wars = [list(input().rstrip()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    who = wars[i][j]
    cnt = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and wars[nx][ny] == who:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    if who == 'W':
        return cnt, 0
    return 0, cnt

our = enemy = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            a, b = bfs(i,j)
            our += a*a
            enemy += b*b
print(our, enemy)