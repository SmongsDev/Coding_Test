import sys; input = sys.stdin.readline
n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
res = 0
for t in range(n):
    give = tips[t] - t
    res += give if give > 0 else 0
print(res)