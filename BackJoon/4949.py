import sys

while 1:
    N = sys.stdin.readline().rstrip()
    
    if N == '.':
        break
        
    stack = []
    
    for i in N:
        if '(' == i or '[' == i:
            stack.append(i)
        elif ')' == i:
            if not stack or stack[-1] == '[':
                print('no')
                break
            else:
                stack.pop()
        elif ']' == i:
            if not stack or stack[-1] == '(':
                print('no')
                break
            else:
                stack.pop()
            
    else:
        if stack:
            print("no")
        else:
            print('yes')
