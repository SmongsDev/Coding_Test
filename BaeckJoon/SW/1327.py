import sys; input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n, k = map(int,input().split())
nums = list(input().split())
target = sorted(nums)
visited = set(''.join(nums))

res = INF
q = deque()
q.append((nums,0))
while q:
    arr, cnt = q.popleft()
    if target == arr:
        res = cnt
        break
    for i in range(n-k+1):
        rar = arr[i:i+k]
        rar.reverse()
        tmp = arr[:i] + rar + arr[i+k:]
        check = ''.join(tmp)
        if check not in visited:
            visited.add(check)
            q.append((tmp,cnt+1))

if res == INF:
    print(-1)
else:
    print(res)