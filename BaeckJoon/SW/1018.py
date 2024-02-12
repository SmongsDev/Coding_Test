import sys; input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
res = []
for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
        for x in range(i,i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        case1 += 1
                    else:
                        case2 += 1
                else:
                    if board[x][y] != 'B':
                        case1 += 1
                    else:
                        case2 += 1
        res.append(min(case1, case2))
print(min(res))