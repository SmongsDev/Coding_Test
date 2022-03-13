n = int(input())

def hetop(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hetop(n-1, a, c, b)
        print(a, c)
        hetop(n-1, b, a, c)

s = 1

for i in range(n - 1):
    s = s * 2 + 1

print(s)
hetop(n, 1, 2, 3)
