import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
A = [list(map(int,input().rstrip())) for _ in range(n)]
B = [list(map(int,input().rstrip())) for _ in range(n)]

def bfs(x,y):
    for i in range(3):
        for j in range(3):
            nx,ny = x+i, y+j
            if A[nx][ny] == 1:
                A[nx][ny] = 0
            else:
                A[nx][ny] = 1

res = 0
if (n < 3 or m < 3) and A != B:
    res = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                bfs(i,j)
                res += 1
if res != -1:
    if A != B:
        res = -1
print(res)