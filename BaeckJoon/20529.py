from itertools import combinations

def sum(a, b):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(input().split())
    result = 0
    cnt = []
    if len(arr) > 32:
        print(0)
        continue    
    for a, b, c in combinations(arr,3):
        tmp = sum(a,b) + sum(b,c) + sum(a,c)
        cnt.append(tmp)
    cnt.sort()
    print(cnt[0])