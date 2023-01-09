N = int(input())
idx = 0
lst = []
result = []

for _ in range(N):
    push = int(input())
    
    while push > idx:
        idx += 1
        lst.append(idx)
        result.append('+')
        
    if lst[-1] == push:
        lst.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

print(*result, sep="\n")
