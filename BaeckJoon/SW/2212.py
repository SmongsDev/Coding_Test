import sys; input = sys.stdin.readline
n = int(input())
k = int(input())
food_stores = list(map(int, input().split()))
food_stores.sort()

diff = []
for i in range(n-1):
    diff.append(food_stores[i+1] - food_stores[i])

diff.sort()
result = 0
for i in range(n-k):
    result += diff[i]
print(result)