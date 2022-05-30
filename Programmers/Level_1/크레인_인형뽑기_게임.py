def solution(board, moves):
    answer = []
    result = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                answer.append(board[j][i-1])
                board[j][i-1] = 0
                if answer[-1:] == answer[-2:-1]:
                    result += 2
                    answer = answer[:-2]
                break
    
    return result