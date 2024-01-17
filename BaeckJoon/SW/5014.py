import sys; input = sys.stdin.readline
from collections import deque
f,s,g,u,d = map(int, input().split())
visited = [0] * (f+1)

q = deque()
q.append(s)
while q:
    if visited[g]:
        print(visited[g]-1)
        break
    now = q.popleft()
    for i in now+u, now-d:
        if 0 < i <= f and not visited[i]:
            visited[i] = visited[now] + 1
            q.append(i)
else:
    print('use the stairs')