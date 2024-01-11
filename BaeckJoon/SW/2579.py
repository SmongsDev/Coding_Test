n = int(input())
step = [0] * 301
dp = [0] * 301
for i in range(1,n+1):
    step[i] = int(input())
dp[1] = step[1]
dp[2] = step[1] + step[2]
dp[3] = max(dp[1] + step[3], step[2] + step[3])
for i in range(4,n+1):
    dp[i] = max(step[i] + dp[i-2], step[i] + step[i-1] + dp[i-3])
print(dp[n])