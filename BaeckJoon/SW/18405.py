from collections import deque
import sys; input = sys.stdin.readline
n, k = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
s, sx, sy = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_lst.append((graph[i][j],i,j))
virus_lst.sort()
time = 0
d = deque(virus_lst)
while d:
    if time == s:
        break
    for _ in range(len(d)):
        virus, x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                d.append((virus, nx, ny))
    time += 1
print(graph[sx-1][sy-1])