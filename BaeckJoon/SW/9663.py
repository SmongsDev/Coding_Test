n = int(input())
graph = [[0]*n for _ in range(n)]

visited = [[0]*n for _ in range(n)]
arr = []

def disable(x, y):
    for i in range(n):
        visited[x][i] = 1
        visited[i][y] = 1
        px = x + i
        py = y + i
        mx = x - i
        my = y - i
        if 0 <= px < n and 0 <= py < n:
            visited[px][py] = 1
        if 0 <= mx < n and 0 <= my < n:
            visited[mx][my] = 1
        if 0 <= px < n and 0 <= my < n:
            visited[px][my] = 1
        if 0 <= mx < n and 0 <= py < n:
            visited[mx][py] = 1

def back(x, y):
    return
    
for i in range(n):
    for j in range(n):
        back(i,j)
print(visited)