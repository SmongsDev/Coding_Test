import sys; input = sys.stdin.readline
from collections import deque
s = input().rstrip()
result = []
isReverse = False
stack = deque()
for i in s:
    if not isReverse:
        if i == '<':
            isReverse = True
            while stack:
                result.append(stack.pop())
            result += i
        elif i == ' ':
            while stack:
                result.append(stack.pop())
            result.append(' ')
        else:
            stack.append(i)
    else:
        result += i
        if i == '>':
            isReverse = False
while stack:
    result.append(stack.pop())
print(''.join(result))