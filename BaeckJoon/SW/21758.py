import sys; input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
sum_lst = [lst[0]]
for i in range(1,n):
    sum_lst.append(sum_lst[i-1] + lst[i])
res = 0

# 꿀벌벌
for i in range(1,n-1):
    res = max(res, sum_lst[n-2] + sum_lst[i-1] - lst[i])

# 벌꿀벌
for i in range(1,n-1):
    res = max(res, sum_lst[n-2] - lst[0] + lst[i])

# 벌벌꿀
for i in range(1,n-1):
    res = max(res, sum_lst[n-1] - lst[0] - lst[i] + sum_lst[n-1] - sum_lst[i])
print(res)