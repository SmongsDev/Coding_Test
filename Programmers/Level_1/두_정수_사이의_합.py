def solution(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    
    return sum([i for i in range(a, b+1)])