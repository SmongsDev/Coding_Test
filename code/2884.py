import sys

h, m = map(int, sys.stdin.readline.split())

m1 = m - 45

if m1 >= 0:
    print(h, m1)

else:
    h = h - 1
    m2 = 60 + m1

    if h >= 0:
        print(h, m2)
    
    else:
        print(23, m2)