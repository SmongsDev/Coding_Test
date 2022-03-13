import math

n = int(input())

def u(n):
    r = n * n * math.pi
    return r

def t(n):
    r = 2 * n * n
    return r

print(format(u(n), ".6f"))
print(format(t(n), ".6f"))
