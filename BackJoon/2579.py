import sys 

input = sys.stdin.readline

T = int(input())
step = [0] * 301
dp = [0] * 301

for i in range(T):
    step[i] = int(input())
    
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0] + step[2], step[1] + step[2])

if T <= 3:
    print(dp[T-1])
    exit(0)

for i in range(3, T+1):
    dp[i] = max(dp[i-2] + step[i], step[i] + step[i-1] + dp[i-3])

print(dp[T-1])
