import sys; input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
visited = [[False]*m for _ in range(n)]

res = 1
visited[r][c] = True
while 1:
    flag = 0
    for _ in range(4):
        d = (d - 1) % 4
        nx = r + directions[d][0]
        ny = c + directions[d][1]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                r, c = nx, ny
                res += 1
                flag = 1
                break
    if flag == 0:
        px = r - directions[d][0]
        py = c - directions[d][1]
        if px < 0 or px >= n or py < 0 or py >= m or board[px][py] == 1:
            break
        r, c = px, py
print(res)