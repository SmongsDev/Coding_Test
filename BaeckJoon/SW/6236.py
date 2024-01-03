import sys; input = sys.stdin.readline
n,m = map(int,input().split())
moneys = [ int(input()) for _ in range(n) ]

start = min(moneys)
end = sum(moneys)
while start <= end:
    mid = (start + end) // 2
    charges = mid
    cnt = 1
    for i in moneys:
        if charges < i:
            cnt += 1
            charges = mid
        charges -= i
    if cnt > m or mid < max(moneys):
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)