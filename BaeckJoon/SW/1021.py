from collections import deque
import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = [ i for i in range(1,n+1) ]
q = deque(nums)

cnt = 0
for target in arr:
    idx = q.index(target)
    if len(q) // 2 >= idx:
        check = q.popleft()
        while target != check:
            cnt += 1
            q.append(check)
            check = q.popleft()
    else:
        check = q.pop()
        while target != check:
            cnt += 1
            q.appendleft(check)
            check = q.pop()
        cnt += 1
print(cnt)