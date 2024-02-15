import sys; input = sys.stdin.readline
INF = int(1e9)
n = int(input())
nums = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())
max_res = -INF
min_res = INF

def dfs(idx, val):
    global max_res, min_res, add, sub, mul, div
    if idx == n:
        max_res = max(max_res, val)
        min_res = min(min_res, val)
        return
    if add > 0:
        add -= 1
        dfs(idx+1, val+nums[idx])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(idx+1, val-nums[idx])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(idx+1, val*nums[idx])
        mul += 1
    if div > 0:
        div -= 1
        dfs(idx+1, int(val/nums[idx]))
        div += 1

dfs(1,nums[0])
print(max_res)
print(min_res)