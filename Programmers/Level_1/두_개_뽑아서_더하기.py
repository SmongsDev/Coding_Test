from itertools import combinations

def solution(numbers):
    arr = []
    for i in combinations(numbers, 2):
        arr.append(sum(i))
    
    return sorted(list(set(arr)), reverse=False)