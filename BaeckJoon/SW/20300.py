import sys; input = sys.stdin.readline
n = int(input())
lst = sorted(list(map(int, input().split())))
res = []
if n % 2 != 0:
    res.append(lst[-1])
    lst = lst[:-1]
for i in range(len(lst)//2):
    res.append(lst[i] + lst[(len(lst)-1)-i])
print(max(res))