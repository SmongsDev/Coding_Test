n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

result = 0
dp = [0] * (n+1)
for i in range(n-1,-1,-1):
    time = arr[i][0] + i
    if time <= n:
        dp[i] = max(result, arr[i][1] + dp[time])
        result = dp[i]
    else:
        dp[i] = result
print(result)