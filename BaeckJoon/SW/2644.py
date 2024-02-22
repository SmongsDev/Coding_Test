from collections import deque
n = int(input())
start, end = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
q = deque([(start,0)])
visited[start] = True
while q:
    now, cost = q.popleft()
    if now == end:
        print(cost)
        break
    for nex in graph[now]:
        if not visited[nex]:
            visited[nex] = True
            q.append((nex,cost+1))
else:
    print(-1)