import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for _ in range(n+m):
    tmp = input().rstrip()
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

res = []
for k, v in dic.items():
    if v > 1:
        res.append(k)

res.sort()
print(len(res))
for i in res:
    print(i)