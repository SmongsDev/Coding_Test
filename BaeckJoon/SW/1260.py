from collections import deque
n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1)
def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
dfs(v)
print()

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
bfs(v)