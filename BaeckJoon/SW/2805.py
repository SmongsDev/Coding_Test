import sys; input = sys.stdin.readline
n, m = map(int,input().split())
woods = list(map(int,input().split()))

res = 0
start = 1
end = max(woods)
while start <= end:
    mid = (start + end) // 2
    length = 0
    for wood in woods:
        length += wood - mid if wood > mid else 0
    
    if length >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)