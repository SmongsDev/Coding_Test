n = int(input())
cards = [0] + list(map(int, input().split()))
cost = [0] * (n+1)

for pack in range(1, n+1):
    for j in range(1, pack+1):
        cost[pack] = max(cost[pack], cost[pack-j] + cards[j])
print(cost[n])