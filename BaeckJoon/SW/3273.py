n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

cnt = 0

start = 0
end = n-1
while start < end:
    result = arr[start] + arr[end]
    if result == x:
        cnt += 1
        end -= 1
    elif result < x:
        start += 1
    elif result > x:
        end -= 1
print(cnt)