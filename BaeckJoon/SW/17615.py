import sys; input = sys.stdin.readline
n = int(input())
bolls = input().rstrip()
res = [0,0,0,0]

cnt_lst = []
cnt = 1
for b in range(1,len(bolls)):
    if bolls[b] != bolls[b-1]:
        cnt_lst.append(cnt)
        cnt = 1
    else:
        cnt += 1
if cnt != 0:
    cnt_lst.append(cnt)

for i in range(1,len(cnt_lst)):
    if i % 2 != 0:
        res[0] += cnt_lst[i]
    else:
        res[1] += cnt_lst[i]

cnt_lst.reverse()
for i in range(1,len(cnt_lst)):
    if i % 2 != 0:
        res[2] += cnt_lst[i]
    else:
        res[3] += cnt_lst[i]
print(min(res))