import sys; input = sys.stdin.readline
INF = int(1e9)
n = int(input())
dis = list(map(int,input().split()))
costs = list(map(int,input().split()))

res = 0
now = costs[0]
for i in range(n-1):
    res += now * dis[i]
    if now > costs[i+1]:
        now = costs[i+1]
print(res)