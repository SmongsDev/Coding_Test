import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
board = [list(map(int,input().rstrip())) for _ in range(n)]
res = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    board[i][j] = 0
    q = deque([(i,j)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                q.append((nx,ny))
                board[nx][ny] = 0
                cnt += 1
    return cnt
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            res.append(bfs(i,j))
res.sort()
print(len(res))
print(*res, sep='\n')