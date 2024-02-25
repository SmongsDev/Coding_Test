import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
res = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if res[j] == 0 and arr[i] == cnt:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1
print(*res)