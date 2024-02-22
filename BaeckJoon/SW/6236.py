import sys; input = sys.stdin.readline
n, m = map(int,input().split())
moneys = [int(input()) for _ in range(n)]

res = 0
start = min(moneys)
end = sum(moneys)
while start <= end:
    mid = (start + end) // 2
    charge = mid
    cnt = 1
    for money in moneys:
        if charge < money:
            cnt += 1
            charge = mid
        charge -= money
    if cnt > m or mid < max(moneys):
        start = mid + 1
    else:
        end = mid - 1
        res = mid
print(res)