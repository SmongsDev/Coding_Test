import sys; input = sys.stdin.readline
n, c = map(int,input().split())
homes = [ int(input()) for _ in  range(n) ]
homes.sort()

result = 0
start = 1
end = homes[-1] - homes[0]
while start <= end:
    mid = (start + end) // 2
    value = homes[0]
    cnt = 1
    for i in range(1,n):
        if homes[i] >= value + mid:
            cnt += 1
            value = homes[i]
    if cnt >= c:
        start = mid + 1
        result = max(mid, result)
    else:
        end = mid - 1
print(result)