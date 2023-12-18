from itertools import combinations_with_replacement

n, m = map(int, input().split())
# nums = [ i for i in range(1,n+1) ]
# for i in combinations_with_replacement(nums,m):
#     for j in range(len(i)):
#         print(i[j], end=' ')
#     print()

# 다른 풀이 
arr = []
def back():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(1,n+1):
            if len(arr) == 0 or arr[-1] <= i:
                arr.append(i)
                back()
                arr.pop()

back()