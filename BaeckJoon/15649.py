n, m = map(int, input().split())

def d(l):
    if l == m:
        for i in range(l):
            print(r[i], end=' ')
        print()
    else:
        for j in range(1, n+1):
            if ch[j] == 0:
                ch[j] = 1
                r[l] = j
                d(l + 1)
                ch[j] = 0

r = [0] * n
ch = [0] * (n + 1)
d(0)
