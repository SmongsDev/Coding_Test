n1, n2 = map(int, input().split())
c = list(map(int, input().split()))

r = 0

for i in range(n1):
    for j in range(i+1, n1):
        for k in range(j+1, n1):
            if c[i]+c[j]+c[k] <= n2:
                r = max(r, c[i] + c[j] + c[k])

print(r)
