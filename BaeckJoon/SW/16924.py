import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(i,j):
    global res
    q = deque()
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
            q.append((nx,ny,d))
    if len(q) == 4:
        visited[i][j] = 1
    size = 1
    while len(q) == 4:
        res.append((i+1,j+1,size))

        for _ in range(4):
            x, y, d = q.popleft()
            visited[x][y] = 1
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
                q.append((nx,ny,d))
        size += 1

cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            bfs(i,j)
            cnt += 1

_sum = 0
for i in visited:
    _sum += sum(i)

if _sum != cnt:
    print(-1)
else:
    print(len(res))
    for x,y,s in res:
        print(x,y,s)