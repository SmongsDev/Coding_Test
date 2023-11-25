import sys

N = int(sys.stdin.readline())
N_list = []
for i in range(N):
    N_list.append(sys.stdin.readline().rstrip())

sort_list = list(set(N_list))
sort_list.sort()
sort_list.sort(key=len)
print(*sort_list, sep="\n")
