n = int(input())
calums = []
for _ in range(n):
    x, y = map(int,input().split())
    calums.append((x,y))
calums.sort()

tall = 0
for i in range(n):
    if calums[i][1] > calums[tall][1]:
        tall = i

area = calums[tall][1]
height = calums[0][1]
for i in range(tall):
    area += height * (calums[i+1][0] - calums[i][0])
    if height < calums[i+1][1]:
        height = calums[i+1][1]

height = calums[-1][1]
for i in range(n-1,tall,-1):
    area += height * (calums[i][0] - calums[i-1][0])
    if height < calums[i-1][1]:
        height = calums[i-1][1]
print(area)