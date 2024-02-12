import sys; input = sys.stdin.readline
INF = int(1e9)
n, m = map(int,input().split())
fuel = [list(map(int,input().split())) for _ in range(n)]

dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i] = [fuel[0][i]] * 3

for i in range(1,n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 2) or (j == m-1 and k == 0):
                continue
            for l in range(3):
                if k == l:
                    continue
                dp[i][j][k] = min(dp[i][j][k], fuel[i][j] + dp[i-1][j-k+1][l])

res = INF
for i in range(m):
    res = min(min(dp[n-1][i]), res)
print(res)