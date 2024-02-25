import sys; input = sys.stdin.readline
n = int(input())
res = []
for _ in range(n):
    x, y = map(int,input().split())
    res.append([x,y,1])
for i in res:
    for j in res:
        if i[0] < j[0] and i[1] < j[1]:
            i[2] += 1
for i in res:
    print(i[2], end=' ')