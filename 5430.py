import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

check = False
for _ in range(T):
    p = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    if '' in arr:
        arr.pop()
        
    reverse_cnt = 0
    for i in p:
        if i == 'R':
            reverse_cnt += 1
        if i == 'D':
            if not arr:
                print('error')
                check = True
                break
            else:
                if reverse_cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    if not check:
        if reverse_cnt % 2 != 0:
            arr.reverse()
        print('[',','.join(map(str,arr)) ,']', sep='')
    else:
        check = False