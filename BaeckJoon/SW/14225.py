import sys; input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

result = 1
for i in arr:
    if i > result:
        break
    result += i
print(result)