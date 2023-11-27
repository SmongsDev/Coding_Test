from itertools import permutations

n, m = map(int, input().split())
# nums = [ i for i in range(1, n+1) ]
# lst = list(permutations(nums, m))
# for i in lst:
#     for j in i:
#         print(j, end=' ')
#     print()

# 라이브러리 안쓰고

arr = []
def backTracking():
    if m == len(arr):
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(1,n+1):
            if i not in arr:
                arr.append(i)
                backTracking()
                arr.pop()

backTracking()