from collections import deque
import sys; input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

ice_mountain = [(i,j) for i in range(n) for j in range(m) if graph[i][j] != 0]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    seaList = []
    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x,y,sea))
    for x, y, sea in seaList:
        graph[x][y] -= sea
        if graph[x][y] < 0:
            graph[x][y] = 0
    return True

time = 0
while ice_mountain:
    ice_cnt = 0
    melt_ice = []
    visited = [[False] * m for _ in range(n)]
    for x, y in ice_mountain:
        if graph[x][y] and not visited[x][y]:
            bfs(x,y)
            ice_cnt += 1
        if graph[x][y] == 0:
            melt_ice.append((x,y))
    if ice_cnt >= 2:
        print(time)
        break
    ice_mountain = list(set(ice_mountain) - set(melt_ice))
    time += 1

if ice_cnt < 2:
    print(0)