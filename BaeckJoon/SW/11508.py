import sys; input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
res = 0
for i in range(0,n,3):
    res += sum(lst[i:i+2])
print(res)