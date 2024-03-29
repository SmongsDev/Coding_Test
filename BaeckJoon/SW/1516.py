import sys; input = sys.stdin.readline
from collections import deque
from copy import deepcopy
n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
for i in range(1,n+1):
    request = list(map(int,input().split()))
    time[i] = request[0]
    for j in request[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    result = deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)                
    for i in result[1:]:
        print(i)
topology_sort()