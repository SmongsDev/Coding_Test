def solution(d, budget):
    s = 0
    d.sort()
    for i in d:
        if i <= budget:
            budget -= i
            s += 1
    return s