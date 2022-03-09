import sys

t, m = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

sum = (m + n) // 60
result = (m + n) % 60

if sum > 0:
    t = t + sum

    if t >= 24:
        t = t - 24
        print(str(t) + ' ' + str(result))
    else:
        print(str(t) + ' ' + str(result))

else:
    print(str(t) + ' ' + str(result))