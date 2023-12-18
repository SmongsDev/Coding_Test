from itertools import combinations
n, s = map(int,input().split())
nums = list(map(int, input().split()))

cnt = 0
# arr = []
# def back(length, depth):
#     global cnt
#     if len(arr) == length:
#         if sum(arr) == s:
#             cnt += 1
#         return
#     else:
#         for i in range(depth, n):
#             if nums[i] not in arr:
#                 arr.append(nums[i])
#                 back(length, i+1)
#                 arr.pop()

for i in range(2,n+1):
#     back(i, 0)
    for j in combinations(nums,i):
        if sum(j) == s:
            cnt += 1
print(cnt)