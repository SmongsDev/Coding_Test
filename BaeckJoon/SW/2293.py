n, k = map(int, input().split())
coins = []
d = [0] * 100001

for i in range(n):
    coins.append(int(input()))

for coin in coins:
    for j in range(coin, k+1):
        d[j] = max(d[j], d[j - coin] + 1)
print(d[k])