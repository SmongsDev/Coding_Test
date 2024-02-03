import sys; input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))
res = arr[-1]
for i in arr[:-1]:
    res += i/2
print('{:g}'.format(res))