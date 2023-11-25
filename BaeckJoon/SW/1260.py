from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [ [] for _ in range(n+1) ]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(m):
    graph[i].sort()

# dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

# def dfs(start):
#     if not graph[v]:
#         return

#     dfs_visited[start] = True
#     print(start, end=' ')
#     for i in graph[start]:
#         if not dfs_visited[i]:
#             dfs(i)

def dfs(start):
    if not graph[v]:
        return
    stack = deque([start])
    visited = []
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            tmp = []
            for i in graph[now]:
                if i not in visited:
                    tmp.append(i)
            tmp.sort(reverse=True)
            stack += tmp

    print(' '.join(map(str, visited)))

def bfs(start):
    if not graph[v]:
        return
    que = deque([start])
    bfs_visited[start] = True

    while que:
        next = que.popleft()
        print(next, end=' ')
        for i in graph[next]:
            if not bfs_visited[i]:
                que.append(i)
                bfs_visited[i] = True

dfs(v)
bfs(v)