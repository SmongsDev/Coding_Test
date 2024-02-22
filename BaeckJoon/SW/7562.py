import sys; input = sys.stdin.readline
from collections import deque
directions = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
for _ in range(int(input())):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    position_x, position_y = map(int,input().split())
    target_x, target_y = map(int,input().split())

    q = deque([(position_x, position_y, 0)])
    board[position_x][position_y] = 1
    while q:
        x, y, move = q.popleft()
        if x == target_x and y == target_y:
            print(move)
            break
        for i in range(8):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx,ny,move+1))