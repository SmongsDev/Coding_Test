import sys; input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        board[a][b] = 1
    
    res = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                res += 1
                q = deque([(i,j)])
                board[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                            board[nx][ny] = 0
                            q.append((nx,ny))
    print(res)