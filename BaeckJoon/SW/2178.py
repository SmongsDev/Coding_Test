import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque([(0,0)])
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            q.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1
print(graph[n-1][m-1])