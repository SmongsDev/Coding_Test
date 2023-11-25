n = int(input())
d = [0] * n

for i in range(n):
    d[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i-1][j] + d[i][j]
        elif j == len(d[i]) - 1:
            d[i][j] = d[i-1][j-1] + d[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]
print(max(d[n-1]))