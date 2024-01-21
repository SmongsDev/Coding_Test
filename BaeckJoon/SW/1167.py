import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
trees = [[] for _ in range(n+1)]
for i in range(n):
    request = list(map(int, input().split()))
    for i in range(1, len(request)-1, 2):
        trees[request[0]].append((request[i], request[i+1]))

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (n+1)
    visited[start] = 0
    res = [0, 0]
    while q:
        now, dist = q.popleft()
        for nex, d in trees[now]:
            if visited[nex] == -1:
                cost = d + dist
                visited[nex] = cost
                q.append((nex, cost))
                if res[1] < cost:
                    res[0] = nex
                    res[1] = cost
    return res
u_node, u_dist = bfs(1)
print(bfs(u_node)[1])
