n = int(input())
d = [0] * (n+1)
step = [0] * (n+1)
for i in range(n):
    step[i] = int(input())

d[0] = step[0]
d[1] = max(step[1], step[0]+step[1])
if n < 2:
    print(d[n-1])
else:
    d[2] = max(step[0]+step[2], step[1]+step[2])
    for i in range(3, n+1):
        d[i] = max(d[i-2] + step[i], d[i-3] + step[i-1] + step[i]) 
    print(d[n-1])