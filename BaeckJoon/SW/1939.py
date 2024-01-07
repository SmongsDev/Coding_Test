from heapq import heappush, heappop
import sys; input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
for i in range(n+1):
    graph[i].sort(reverse=True)
start, end = map(int, input().split())
h = []
distance = [0] * (n+1)
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
    for w, nex in graph[now]:
        if weight == 0:
            distance[nex] = w
            heappush(h, (-distance[nex], nex))
        if distance[nex] < w and distance[nex] < weight:
            distance[nex] = min(weight, w)
            heappush(h,(-distance[nex], nex))