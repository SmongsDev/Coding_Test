a, b, v = map(int, input().split())

day = (v - b) // (a - b)

if (v - b) % (a - b) == 0:
    print(day)

else:
    print(day + 1)
