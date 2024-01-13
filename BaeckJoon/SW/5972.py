from heapq import heappush, heappop
import sys; input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [INF] * (n+1)
h = []
heappush(h,(0,1))
distance[1] = 0
while h:
    dist, now = heappop(h)

    if distance[now] < dist:
        continue
    for nex, d in graph[now]:
        cost = dist + d
        if distance[nex] > cost:
            distance[nex] = cost
            heappush(h, (cost, nex))
print(distance[-1])