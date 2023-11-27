from itertools import combinations

n, m = map(int,input().split())
# nums = [ i for i in range(1,n+1) ]
# coms = list(combinations(nums, m))

# for i in coms:
#     for j in i:
#         print(j, end=' ')
#     print()

# 라이브러리 없이

arr = []
def back(depth):
    if m == len(arr):
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(depth, n+1):
            if i not in arr:
                arr.append(i)
                back(i+1)
                arr.pop()
back(1)