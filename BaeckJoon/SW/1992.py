import sys; input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

def divide(row, cal, size):
    if size == 1:
        print(board[row][cal], end='')
        return
    num = board[row][cal]

    for i in range(row,row+size):
        for j in range(cal,cal+size):
            if num != board[i][j]:
                print('(', end='')
                size //= 2
                divide(row, cal, size)
                divide(row, cal+size, size)
                divide(row+size, cal, size)
                divide(row+size, cal+size, size)
                print(')', end='')
                return
    print(num, end='')
    return
divide(0,0,n)                