import sys; input = sys.stdin.readline
from itertools import combinations
INF = int(1e9)
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
chicken = [(i,j) for i in range(n) for j in range(n) if board[i][j] == 2]
homes = [(i,j) for i in range(n) for j in range(n) if board[i][j] == 1]

result = INF
for coms in combinations(chicken,m):
    tmp_dis = 0
    for home in homes:
        min_dis = INF
        for i in range(m):
            now_dis = abs(home[0] - coms[i][0]) + abs(home[1] - coms[i][1])
            min_dis = min(min_dis, now_dis)
        tmp_dis += min_dis
    result = min(result, tmp_dis)
print(result)