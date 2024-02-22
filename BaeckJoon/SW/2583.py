import sys; input = sys.stdin.readline
from collections import deque
m, n, k = map(int,input().split())
board = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[x][y] = 1

def bfs(i,j):
    cnt = 1
    board[i][j] = 1
    q = deque([(i,j)])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    return cnt

res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            res.append(bfs(i,j))

res.sort()
print(len(res))
print(*res)