import sys; input = sys.stdin.readline
k, n = map(int,input().split())
lans = [int(input()) for _ in range(k)]

res = 0
start = 1
end = max(lans)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    
    if cnt >= n:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)