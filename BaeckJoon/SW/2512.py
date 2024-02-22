import sys; input = sys.stdin.readline
n = int(input())
city = list(map(int,input().split()))
budget = int(input())

res = 0
start = 1
end = max(city)
while start <= end:
    mid = (start + end) // 2
    charge = 0
    for i in city:
        charge += min(i, mid)
    if charge <= budget:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1
print(res)