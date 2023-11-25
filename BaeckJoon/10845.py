import sys
from collections import deque

N = int(sys.stdin.readline())
lst = deque([])

for i in range(N):
    tmp = sys.stdin.readline().split()
    
    if tmp[0] == 'push':
        lst.append(int(tmp[1]))
    elif tmp[0] == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(lst))
    elif tmp[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    else:
        if lst:
            print(lst.popleft())
        else:
            print(-1)
