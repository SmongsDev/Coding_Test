from collections import deque
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
q = deque()
q.append((start, 0))
visited[start] = True
while q:
    now, cost = q.popleft()

    if now == end:
        print(cost)
        exit(0)
    for i in graph[now]:
        if not visited[i]:
            q.append((i, cost+1))
            visited[i] = True

print(-1)