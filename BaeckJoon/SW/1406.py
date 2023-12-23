import sys; input = sys.stdin.readline
stack = list(input().rstrip())
tmp = []
n = int(input())
for _ in range(n):
    requests = input().rstrip().split()
    if len(requests) == 1:
        if requests[0] == 'L' and stack:
            tmp.append(stack.pop())
        elif requests[0] == 'D' and tmp:
            stack.append(tmp.pop())
        elif requests[0] == 'B' and stack:
            stack.pop()
    else:
        put, x = requests
        stack.append(x)
result = stack + tmp[::-1]
print(''.join(result))