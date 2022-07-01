def solution(N, stages):
    answer = {}
    l = len(stages)
    for i in range(1, N+ 1):
        answer[i] = stages.count(i) / l
        if l - stages.count(i) > 0:
            l = l - stages.count(i)
    return sorted(answer, key= lambda x : answer[x],reverse=True)