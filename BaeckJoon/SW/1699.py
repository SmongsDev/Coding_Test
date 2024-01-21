import sys; input = sys.stdin.readline
n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i//2+1):
        result = i - j * j
        if result < 0:
            break
        if dp[i] > dp[result] + 1:
            dp[i] = dp[result] + 1
print(dp[n])