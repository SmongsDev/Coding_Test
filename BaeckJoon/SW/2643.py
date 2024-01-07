import sys; input = sys.stdin.readline
n = int(input())
papers = []
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        papers.append((a,b))
    else:
        papers.append((b,a))
papers.sort(reverse=True)

dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if papers[i][1] <= papers[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))