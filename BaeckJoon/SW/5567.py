import sys; input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [INF] * (n+1)
q = deque([(1,0)])
distance[1] = 0
while q:
    now, dist = q.popleft()

    if distance[now] < dist:
        continue
    for nex, d in graph[now]:
        cost = d + dist
        if distance[nex] > cost:
            distance[nex] = cost
            q.append((nex,cost))

result = 0
for i in distance:
    if i in range(1,3):
        result += 1
print(result)