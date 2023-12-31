n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()

cnt = 1
start = holes[0]
for i in holes[1:]:
    if i in range(start, start+l):
        continue
    else:
        start = i
        cnt += 1
print(cnt)