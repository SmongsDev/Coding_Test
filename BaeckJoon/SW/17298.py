import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = [0]
result = [-1] * n
for i in range(1,n):
    while stack and arr[i] > arr[stack[-1]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)