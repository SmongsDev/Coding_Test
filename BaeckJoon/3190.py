import sys
from collections import deque

input = sys.stdin.readline

# 동 북 서 남
dir = [(0,1), (-1,0), (0,-1), (1,0)]
que = deque([])
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

dic = {}
l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    dic[x] = c

def turn(alpha):    
    global direction
    if alpha == 'D':
        direction = (direction - 1) % 4
    elif alpha == 'L':
        direction = (direction + 1) % 4

x, y = 0, 0
time_cnt = 0
direction = 0

while True:
    time_cnt += 1
    d = dir[direction]
    x += d[0]
    y += d[1]

    if 0 > x or x >= n or 0 > y or y >= n:
        break
    if board[x][y] == 2:
        break
    else:
        if board[x][y] == 1:
            board[x][y] == 2
            que.append((x,y))
            if time_cnt in dic:
                turn(dic[time_cnt])
        else:
            board[x][y] == 2
            que.append((x,y))
            tx, ty = que.popleft()
            board[tx][ty] = 0
            if time_cnt in dic:
                turn(dic[time_cnt])
print(time_cnt)

        