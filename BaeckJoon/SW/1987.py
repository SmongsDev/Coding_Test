import sys; input = sys.stdin.readline
from collections import deque
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0
q = set()
q.add((0,0,graph[0][0]))
while q:
    x, y, dist = q.pop()
    result = max(result, len(dist))
    print(x,y,'==>',dist)
    if result == 26:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in dist:
            q.add((nx,ny,dist+graph[nx][ny]))
print(result)