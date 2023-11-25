import sys

while 1:
    x, y, z = map(int, sys.stdin.readline().split())

    if x == 0 and y == 0 and z == 0:
        break

    arr = [x, y, z]
    arr.sort(reverse=False)

    if (arr[0] ** 2 + arr[1] ** 2) == arr[2] ** 2:
        print("right")
    else:
        print("wrong")