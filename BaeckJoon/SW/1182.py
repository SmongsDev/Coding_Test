import sys; input = sys.stdin.readline
from itertools import combinations 
n, s = map(int,input().split())
arr = list(map(int,input().split()))
res = 0
for i in range(1,n+1):
    for coms in list(combinations(arr,i)):
        if sum(coms) == s:
            res += 1
print(res)