import sys; input = sys.stdin.readline
from heapq import heappush, heappop
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
for i in range(m):
    graph[i].sort(reverse=True)

start, end = map(int, input().split())

weights = [0] * (n+1)
h = []
heappush(h,(0, start))
while h:
    weight, now = heappop(h)
    weight *= -1

    if now == end:
        print(weight)
        break
    if weights[now] > weight:
        continue
    for w, next in graph[now]:
        if weight == 0:
            weights[next] = w
            heappush(h, (-weights[next], next))
        if weights[next] < w and weights[next] < weight:
            weights[next] = min(w, weight)
            heappush(h,(-weights[next], next))