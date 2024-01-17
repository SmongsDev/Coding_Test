import sys; input = sys.stdin.readline
from collections import deque
distance = [(-2,-1),(-1,-2),(-1,2),(-2,1),(2,1),(1,2),(2,-1),(1,-2)]
for _ in range(int(input())):
    l = int(input())
    visited = [[False] * l for _ in range(l)]
    night_x, night_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())
    
    result = 0
    visited[night_x][night_y] = 0

    q = deque()
    q.append((night_x,night_y, 0))
    while q:
        x, y, dist = q.popleft()

        if x == goal_x and y == goal_y:
            result = dist
            break

        for i in range(8):
            nx = x + distance[i][0]
            ny = y + distance[i][1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,dist+1))

    print(result)