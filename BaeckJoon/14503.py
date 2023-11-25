import sys

input = sys.stdin.readline

n, m = map(int, input().split())

x, y, d = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

clean_cnt = 1

visited = [ [False] * m for _ in range(n) ]

def left():
    global d
    d -= 1
    if d < 0:
        d = 3

def dfs(x, y):
    global clean_cnt
    visited[x][y] = True
    check = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if visited[tx][ty] or graph[tx][ty] == 1:
            check += 1
    if check == 4:
        tx = x + dx[d-2]
        ty = y + dy[d-2]
        if graph[tx][ty] == 1:
            return
        else:
            dfs(tx, ty)
    else:
        left()

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] == 0:
                clean_cnt += 1
                dfs(nx, ny)
            else:
                dfs(x,y)
                
    
dfs(x, y)
print(clean_cnt)