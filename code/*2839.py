n = int(input())
rs = 0

while True:
    if n % 5 == 0:
        rs = rs + n // 5
        print(rs)
        break

    n -= 3
    rs += 1

    if n < 0:
        print(-1)
        break
