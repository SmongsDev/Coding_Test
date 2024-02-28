import sys; input = sys.stdin.readline
while 1:
    s = input().rstrip()
    if s == 'end':
        break
    board = []
    for i in range(0,9,3):
        board.append(s[i:i+3])

    check = 0
    o_c = x_c = 0
    for i in board:
        o_c = i.count('O')
        x_c = i.count('X')
        if '.' in i:
            print('invalid')
            check = 1
    if check == 0:
        if x_c < o_c:
            print('invalid')
            continue
        
        flag = 0
        for i in range(3):
            compare = board[i][0]
            cnt = 1
            for j in range(1,3):
                if compare == board[i][j]:
                    cnt += 1
            if cnt == 3:
                flag = 1
        for i in range(3):
            compare = board[0][i]
            cnt = 1
            for j in range(1,3):
                if compare == board[j][i]:
                    cnt += 1
            if cnt == 3:
                flag = 1
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            flag = 1
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            flag = 1
        if flag == 1:
            print('valid')
        else:
            print('invalid')
# 0 1 2 3 4 5 6 7 8


# 0 1 2
# 3 4 5
# 6 7 8