import sys

n, m, o = map(int, sys.stdin.readline().split())
sum = 0

if n == m and m == o:
    sum = 10000 + n * 1000
    print(sum)

elif n == m or n == o:
    sum = 1000 + n * 100
    print(sum)

elif m == o:
    sum = 1000 + m * 100
    print(sum)

else:
    p = max(n, m ,o)
    sum = p * 100
    print(sum)
