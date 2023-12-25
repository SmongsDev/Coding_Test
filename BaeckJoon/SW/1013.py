import re
import sys; input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    s = input().rstrip()    
    if p.fullmatch(s):
        print('YES')
    else:
        print('NO')