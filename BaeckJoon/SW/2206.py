import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
maps = [ list(map(int,input().rstrip())) for _ in range(n) ]

# INF = int(1e9)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
def bfs(s,e):
    d = deque([(s,e,0)])
    visited[s][e][0] = 1
    while d:
        x, y, p = d.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][p]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and visited[nx][ny][p] == 0:
                    d.append((nx,ny,p))
                    visited[nx][ny][p] = visited[x][y][p] + 1
                elif maps[nx][ny] == 1 and p == 0:
                    d.append((nx,ny,p+1))
                    visited[nx][ny][1] = visited[x][y][p] + 1
    return -1

print(bfs(0,0))