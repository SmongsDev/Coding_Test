import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 1, 3, 5, 11]

if n <= 4:
    print(dp[n] % 10007)
    exit(0)

for i in range(5, n+1):
    dp.append(dp[i-1] + (dp[i-2] * 2))
    
print(dp[n] % 10007)
