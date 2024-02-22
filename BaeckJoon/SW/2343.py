import sys; input = sys.stdin.readline
n, m = map(int,input().split())
lessons = list(map(int,input().split()))

res = 0
start = max(lessons)
end = sum(lessons)
while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 1
    for i in lessons:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i
    if cnt <= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)
