n, k = map(int, input().split())
coins = []
d = [0] * (k+1)

d[0] = 1
for i in range(n):
    coins.append(int(input()))

for coin in coins:
    for j in range(coin, k+1):
        d[j] += d[j - coin]
print(d[k])