import sys; input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())

distance = [INF] * (n+1)
distance[start] = 0
q = deque()
q.append((start, 0))
while q:
    now, dist = q.popleft()
    if distance[now] < dist:
        continue
    for nex, d in graph[now]:
        cost = dist + d
        if distance[nex] > cost:
            distance[nex] = cost
            q.append((nex, cost))
print(distance[end])