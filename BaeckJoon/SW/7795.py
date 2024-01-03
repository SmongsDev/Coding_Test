from bisect import bisect_right
import sys; input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A_lst = sorted(list(map(int, input().split())))
    B_lst = sorted(list(map(int, input().split())))
    cnt = [0] * (n)

    for i in range(n):
        cnt[i] = bisect_right(B_lst, A_lst[i]-1)
    print(sum(cnt))