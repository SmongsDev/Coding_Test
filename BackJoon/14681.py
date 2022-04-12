import sys

n, m = map(int, sys.stdin.readline().split())

if n > 0:
    if m > 0:
        print(1)
    else:
        print(4)

else:
    if m > 0:
        print(2)
    else:
        print(3)