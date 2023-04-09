import sys

input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]
lst.sort()

dic = {i: 0 for i in lst}
for i in lst:
    dic[i] += 1
    
mx = max(dic.values())
mx_lst = []

for i in dic:
    if mx == dic[i]:
        mx_lst.append(i)

print(round(sum(lst) / N))
print(lst[N//2])
if len(mx_lst) > 1:
    print(mx_lst[1])
else:
    print(mx_lst[0])
print(max(lst) - min(lst))
