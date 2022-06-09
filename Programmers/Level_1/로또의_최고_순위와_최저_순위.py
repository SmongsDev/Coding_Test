def solution(lottos, win_nums):
    lo = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    cnt = 0
    _cnt = 0
    for i in lottos:
        if i == 0:
            _cnt += 1
        elif i in win_nums:
            cnt += 1
    answer.append(lo[cnt + _cnt])
    answer.append(lo[cnt])
    return answer