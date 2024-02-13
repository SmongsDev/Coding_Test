import sys; input = sys.stdin.readline
from itertools import combinations
n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]
flowers = [(i,j) for i in range(1,n-1) for j in range(1,n-1)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
res = int(1e9)

def check(coms):
    global res
    visited = []
    cost = 0
    for x, y in coms:
        if (x,y) not in visited:
            visited.append((x,y))
            cost += area[x][y]
            for i in range(4):
                nx = x + directions[i][0]
                ny = y + directions[i][1]
                if (nx,ny) in visited or nx < 0 or nx >= n or ny < 0 or ny >= n:
                    return
                visited.append((nx,ny))
                cost += area[nx][ny]
        else:
            return
    res = min(res,cost)

for coms in list(combinations(flowers,3)):
    check(coms)
print(res)