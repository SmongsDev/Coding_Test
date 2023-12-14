from collections import deque
from itertools import combinations
import sys; input = sys.stdin.readline

directions = [(-1,0),(0,1),(1,0),(0,-1)]

n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

empty = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 0]
vir = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 2]

result = 0
for coms in combinations(empty, 3):
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                tmp[i][j] = 1
    for x, y in coms:
        tmp[x][y] = 1
    virus = deque(vir)
    while virus:
        x, y = virus.popleft()
        tmp[x][y] = 2
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus.append((nx,ny))
    cnt = 0
    for i in tmp:
        cnt += i.count(0)
    result = max(result, cnt)
print(result)