import sys

input = sys.stdin.readline

T = int(input())
lst = [0, 1, 2, 4] + ([0] * 7)

def caseNum(n):
    if n == 1:
        return lst[1]
    elif n == 2:
        return lst[2]
    elif n == 3:
        return lst[3]
    else:
        for i in range(4, n+1):
            lst[i] = lst[i-1]+lst[i-2]+lst[i-3]
    
    return lst[n]

for i in range(T):
    n = int(input())
    
    print(caseNum(n))
