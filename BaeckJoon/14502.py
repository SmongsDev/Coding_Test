from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def score(visited):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt

result = 0
def virus():
    visited = [ [0] * m for _ in range(n) ]    
    global result
    
    deq = deque()    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                visited[i][j] = 1
                deq.append((i,j))
                
    while deq:
        x,y = deq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    deq.append((nx,ny))
    result = max(result, score(visited))

def dfs_wall(w):
    if w == 3:
        virus()
        return
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    dfs_wall(w+1)
                    arr[i][j] = 0

dfs_wall(0)

print(result)