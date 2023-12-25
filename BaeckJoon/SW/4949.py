import sys; input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s == '.':
        break

    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')