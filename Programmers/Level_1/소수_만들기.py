from itertools import combinations

def solution(nums):
    count = 0
    com = list(combinations(nums, 3))
    for i in com:
        s = sum(i)
        isT = True
        for j in range(2, s):
            if s % j == 0:
                isT = False
                break
        if isT == True:
            count += 1
    return count