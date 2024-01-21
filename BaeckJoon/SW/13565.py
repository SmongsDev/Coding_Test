import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i):
    global result
    q = deque()
    q.append((0,i))
    graph[0][i] = 1
    while q:
        x, y = q.popleft()
        if x == n-1:
            result = 'YES'
            return 

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny))

result = 'NO'
for i in range(m):
    if graph[0][i] != 1:
        if bfs(i):
            break
print(result)