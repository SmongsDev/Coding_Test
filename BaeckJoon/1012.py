import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return 
    if arr[x][y] == 0:
        return
    arr[x][y] = 0
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

n = int(sys.stdin.readline())

for _ in range(n):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    
    for i in range(K):
        m, n = map(int, sys.stdin.readline().split())
        arr[n][m] = 1

    worm = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dfs(i, j)
                worm += 1
    print(worm)
