n = int(input())
stack = []
now = 1
result = []
check = False
for i in range(1, n+1):
    put = int(input())
    if now < put:
        for j in range(now,put+1):
            stack.append(now)
            result.append('+')
            now += 1
        result.append('-')
        stack.pop()
    else:
        if put in stack:
            for j in range(stack[-1]-put):
                stack.pop()
                result.append('-')
        else:
            check = True
if check:
    print('NO')
else:
    for i in result:
        print(i)