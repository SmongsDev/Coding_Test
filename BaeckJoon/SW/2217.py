import sys; input = sys.stdin.readline
n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
res = 0
for r in ropes:
    res = max(res, r*n)
    n -= 1
print(res)