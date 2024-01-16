from collections import deque
import sys; input = sys.stdin.readline
INF = int(1e9)
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))

distance = [INF]  * (n+1)
distance[x] = 0
q = deque()
q.append((x,0))
while q:
    now, dist = q.popleft()

    if distance[now] < dist:
        continue
    for nex, d in graph[now]:
        cost = dist + d
        if distance[nex] > cost:
            distance[nex] = cost
            q.append((nex, cost))

result = []
for i in range(n+1):
    if distance[i] == k:
        result.append(i)
if not result:
    print(-1)
else:
    print(*sorted(result), sep='\n')