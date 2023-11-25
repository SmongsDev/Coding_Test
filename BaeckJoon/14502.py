from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    cnt += arr[i].count(0)

max_result = 0
def virus():
    visited = [ [0] * m for _ in range(n) ]
    
    global max_result
    
    deq = deque()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                visited[i][j] = 1
                deq.append((i,j))
                
    result = 0
    while deq:
        x,y = deq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                deq.append((nx,ny))
                result += 1
    
    max_result = max(max_result, cnt-result)

def dfs_wall(w):
    if w == 3:
        virus()
        return
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] == 1
                    dfs_wall(w+1)
                    arr[i][j] = 0

dfs_wall(0)

print(max_result-3)