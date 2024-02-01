import sys; input = sys.stdin.readline
from heapq import heappush, heappop
INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heappush(q,(0,start))
    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue
        
        for nex, d in graph[now]:
            cost = dist + d
            if distance[nex] > cost:
                distance[nex] = cost
                heappush(q,(cost,nex))
    return distance

v1, v2 = map(int,input().split())

v_0 = dijkstra(1)
v_1 = dijkstra(v1)
v_2 = dijkstra(v2)

res_1 = v_0[v1] + v_1[v2] + v_2[n]
res_2 = v_0[v2] + v_2[v1] + v_1[n]
res = min(res_1, res_2)
print(res if res < INF else -1)