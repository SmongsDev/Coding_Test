n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a][b] = c

print(graph)
# def dfs():
