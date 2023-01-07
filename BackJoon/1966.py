import sys
from collections import deque

caseNum = int(sys.stdin.readline())

for i in range(caseNum):
    n, m = map(int, sys.stdin.readline().split())
    lst = deque(list(map(int, sys.stdin.readline().split())))
    
    count = 0
    while lst:
        big = max(lst)
        front = lst.popleft()
        m -= 1
        
        if big == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            lst.append(front)
            if m < 0:
                m = len(lst) - 1
