n = int(input())

arr = []

for i in range(n):
    x, y =  map(int, input().split())
    arr.append([x, y, 1])

for i in arr:
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            i[2] += 1

for i in arr:
    print(i[2], end=' ')
