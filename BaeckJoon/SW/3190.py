import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
k = int(input())
apples = [ list(map(int, input().split())) for _ in range(k) ]
l = int(input())
turns = []
for i in range(l):
    x, s = input().split()
    turns.append((int(x),s))
visited = [[0]* (n+1) for _ in range(n+1)]
for a, b in apples:
    visited[a][b] = 2
dx = [-1,0,1,0]
dy = [0,1,0,-1]
d = 1

limit = deque(turns)
l_time, turn = limit.popleft()
time = 0
x = y = 1
visited[x][y] = 1
tails = deque([(x,y)])
while True:
    time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if nx <= 0 or nx > n or ny <= 0 or ny > n or visited[nx][ny] == 1:
        break
    if visited[nx][ny] == 0:
        ex, ey = tails.popleft()
        visited[ex][ey] = 0
    visited[nx][ny] = 1
    tails.append((nx,ny))
    x, y = nx, ny
    if time == l_time:
        if turn == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        if limit:
            l_time, turn = limit.popleft()
print(time)