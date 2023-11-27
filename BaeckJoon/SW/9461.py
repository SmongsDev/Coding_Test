T = int(input())
d = [0, 1, 1, 1] + [0] * 97

for i in range(3,101):
    d[i] = d[i-2] + d[i-3]

for i in range(T):
    N = int(input())
    print(d[N])