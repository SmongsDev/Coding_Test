def solution(n, lost, reserve):
    reserve.sort()
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        if i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)