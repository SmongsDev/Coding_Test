import sys; input = sys.stdin.readline
from collections import deque
a, b = map(int,input().split())
q = deque([(a,1)])
while q:
    now, cnt = q.popleft()
    if now == b:
        print(cnt)
        break
    elif now < b:
        q.append((now*2,cnt+1))
        tmp = str(now) + '1'
        q.append((int(tmp),cnt+1))
else:
    print(-1)