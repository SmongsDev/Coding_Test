import sys; input = sys.stdin.readline
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

res = 0
for coin in coins:
    if coin <= k:
        res += k // coin
        k %= coin
print(res)