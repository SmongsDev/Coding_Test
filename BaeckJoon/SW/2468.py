import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
res = 1

def bfs(i,j, deep, visited):
    q = deque([(i,j)])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > deep and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

for deep in range(max(map(max, graph))):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > deep:
                visited[i][j] = True
                bfs(i,j, deep, visited)
                cnt += 1
    res = max(res, cnt)
print(res)