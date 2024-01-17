import sys; input = sys.stdin.readline
from collections import deque
r, c = map(int,input().split())
yard = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(i,j):
    o, v = 0, 0
    if yard[i][j] == 'v':
        v += 1
    elif yard[i][j] == 'o':
        o += 1
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and yard[nx][ny] != '#':
                if yard[nx][ny] == 'v':
                    v += 1
                elif yard[nx][ny] == 'o':
                    o += 1
                q.append((nx,ny))
                visited[nx][ny] = True
    if o <= v:
        return 0, v
    else:
        return o, 0

O, V = 0, 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and yard[i][j] != '#':
            a, b = bfs(i,j)
            O += a
            V += b
print(O,V)