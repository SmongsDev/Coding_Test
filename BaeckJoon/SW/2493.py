import sys; sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

stack = [n-1]
result = [0] * n
for i in range(n-2,-1,-1):
    while stack and arr[i] > arr[stack[-1]]:
        result[stack.pop()] = i+1
    stack.append(i)
print(*result)