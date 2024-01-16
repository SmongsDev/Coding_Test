import sys; input = sys.stdin.readline
INF = int(1e9)
n = int(input())
miro = list(map(int,input().split()))
dp = [INF] * n
dp[0] = 0
for i in range(n):
    for j in range(i+1,i+miro[i]+1):
        if j < n:
            dp[j] = min(dp[j], dp[i] + 1)
if dp[-1] != INF:
    print(dp[-1])
else:
    print(-1)