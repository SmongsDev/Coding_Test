n = int(input())
d = [[1] * 10 for _ in range(n)]

for i in range(1, n):
    for j in range(1, 10):
        d[i][j] = d[i][j-1] + d[i-1][j]

print(sum(d[n-1]) % 10007)