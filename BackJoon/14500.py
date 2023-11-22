# 망

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

# 서 남 동 북
dx = [ 0, 1, 0,-1]
dy = [-1, 0, 1, 0]

data = []

# 4x1
def straight(i, j):
    tmp = []
    d = 1
    if i+3 < n:
        sum = graph[i][j]
        for _ in range(3):
            nx = i + dx[d]
            ny = j + dy[d]
            sum += graph[nx][ny]
        tmp.append(sum)
    d = 2
    if j+3 < m:
        sum = graph[i][j]
        for _ in range(3):
            nx = i + dx[d]
            ny = j + dy[d]
            sum += graph[nx][ny]
        tmp.append(sum)
    
    if tmp:
        data.append(max(tmp))
    else:
        pass

def square(i, j):
    d = 0
    if i+1 < n or j+1 < m:
        sum = graph[i][j]
        for _ in range(3):
            nx = i + dx[d]
            ny = j + dy[d]
            if nx < n and ny < m:
                d += 1
                sum += graph[nx][ny]
        data.append(sum)

def nieun(i,j):
    # L 3시
    for d in range(4):
        sum = 0
        for c in range(4):
            if c == 3:
                if d == 3:
                    d = 0
                else:
                    d += 1
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                sum += graph[nx][ny]
        data.append(sum)

    for d in range(4): 
        sum = 0
        for c in range(4):
            if c == 3:
                d -= 1
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                sum += graph[nx][ny]
        data.append(sum)

def u(i,j):
    for d in range(4):
        sum = 0
        for c in range(4):
            if c == 2:
                nx = i + dx[d-1]
                ny = j + dy[d-1]
                if 0 <= nx < n and 0 <= ny < m:
                    sum += graph[nx][ny] 
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                sum += graph[nx][ny]
        data.append(sum)

def strange(i, j):
    for d in range(4):
        sum = 0
        if d == 1 or d == 2:
            for c in range(4):
                if c == 2:
                    d += 1
                elif c == 3:
                    d -= 1
                nx = i + dx[d]
                ny = j = dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    sum += graph[nx][ny]
        else:
            for c in range(4):
                if c == 2:
                    d -= 1
                elif c == 3:
                    d += 1
                nx = i + dx[d]
                ny = j = dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    sum += graph[nx][ny]
        data.append(sum)

for i in range(n):
    for j in range(m):
        straight(i,j)
        square(i,j)
        nieun(i,j)
        strange(i,j)
        u(i,j)
print(max(data))