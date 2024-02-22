import sys; input = sys.stdin.readline
from collections import deque
n, k = map(int,input().split())
distance = [0] * 100001

q = deque([n])
while q:
    now = q.popleft()
    if now == k:
        print(distance[k])
        break
    for i in [now-1,now+1, now*2]:
        if 0 <= i < 100001 and distance[i] == 0:
            q.append(i)
            distance[i] = distance[now] + 1