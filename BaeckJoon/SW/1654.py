k, n = map(int, input().split())
LAN = [ int(input()) for _ in range(k) ]

start = 1
end = max(LAN)
while start <= end:
    mid = (start + end) // 2
    cable = 0
    for i in LAN:
        cable += i // mid
    if cable < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)