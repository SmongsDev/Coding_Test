import sys
import heapq
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    h = []
    check = False
    for _ in range(n):
        c, x = input().split()
        x = int(x)
        if c == 'I':
            heapq.heappush(h, x)
        else:
            if not h:
                check = True
                continue
            if x == 1:
                heapq.nlargest(1, h)
                heapq.heappop()
            else:
                heapq.nsmallest(1, h)
                heapq.heappop()
    if check:
        print('EMPTY')
    else:
        print(max(h),min(h))