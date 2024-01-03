from heapq import heappush, heappop
import sys; input = sys.stdin.readline
INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start, end = map(int, input().split())
h = []
distance = [-INF] * (n+1)
heappush(h, (0,start))
distance[start] = 0
while h:
    weight, now = heappop(h)
    weight *= -1

    if now == end:
        print(weight)
        break

    if distance[now] > weight:
        continue
    for nex, w in graph[now]:
        max_weight = max(w, weight)
        if distance[nex] < max_weight:
            distance[nex] = max_weight
            heappush(h,(-max_weight, nex))