n = int(input())
idx = 0
stack = []
result = []

for _ in range(n):
    put = int(input())

    while put > idx:
        idx += 1
        stack.append(idx)
        result.append('+')
    
    if stack[-1] == put:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print(*result, sep='\n')