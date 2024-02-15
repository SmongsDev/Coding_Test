import sys; input = sys.stdin.readline
r, c, k = map(int,input().split())
maps = [list(input().rstrip()) for _ in range(r)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
visited = [[False] * c for _ in range(r)]
res = 0
def back(x, y, dist):
    global res
    if x == 0 and y == c-1 and dist == k:
        res += 1
    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'T' and not visited[nx][ny]:
            visited[nx][ny] = True
            back(nx,ny,dist+1)
            visited[nx][ny] = False
visited[r-1][0] = True
back(r-1,0,1)
print(res)