def solution(n):
    answer = ''
    while n > 0:
        n, m = divmod(n, 3)
        answer += str(m)
    return int(answer, 3)