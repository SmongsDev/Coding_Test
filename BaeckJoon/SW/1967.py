import sys; input = sys.stdin.readline
from heapq import heappush, heappop
INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(start):
    res = [0,0]
    visited = [False] * (n+1)
    visited[start] = True
    q = []
    heappush(q,(0,start))
    while q:
        dist, now = heappop(q)
        dist *= -1
        for nex, d in graph[now]:
            cost = dist + d
            if not visited[nex]:
                visited[nex] = True
                heappush(q,(-cost, nex))
                if cost > res[1]:
                    res[0] = nex
                    res[1] = max(cost,res[1])
    return res
v0,e0 = bfs(1)
v1,e1 = bfs(v0)

print(e1)