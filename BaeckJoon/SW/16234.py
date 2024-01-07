from collections import deque
n, l, r = map(int, input().split())
area = [ list(map(int,input().split())) for _ in range(n) ]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
def bfs(a,b):
    q = deque()
    q.append((a,b))
    lst = [(a,b)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                result = abs(area[x][y] - area[nx][ny])
                if l <= result <= r:
                    lst.append((nx,ny))
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return lst

while True:
    visited = [[False] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                country = bfs(i,j)
                
                if len(country) > 1:
                    check = True
                    s = sum(area[x][y] for x,y in country)
                    k = s // len(country)
                    for x,y in country:
                        area[x][y] = k
    if not check:
        break
    cnt += 1
print(cnt)