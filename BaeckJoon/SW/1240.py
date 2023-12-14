from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n+1):
    graph[i].sort()

result = [ list(map(int, input().split())) for _ in range(m) ]
for start, end in result:
    visited = [False] * (n+1)
    q = deque()
    q.append((start,0))
    visited[start] = True
    while q:
        now, total = q.popleft()
        if now == end:
            print(total)
            break

        for cost, next in graph[now]:
            if not visited[next]:
                q.append((next, total+cost))
                visited[next] = True