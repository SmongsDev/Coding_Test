import math

def solution(dartResult):
    answer = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
            print(n)
        elif i == 'S':
            answer.append(int(n))
            n = ''
        elif i == 'D':
            answer.append(math.pow(int(n),2))
            n = ''
        elif i == 'T':
            answer.append(math.pow(int(n),3))
            n = ''
        elif i == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
    return sum(answer)