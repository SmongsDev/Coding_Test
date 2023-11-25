import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n) ]

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
            
result = 9999
for k in combinations(chicken, m):
    tmp = 0
    for i in home:
        min_dis = 9999
        for j in range(m):
            dis = abs(i[0] - k[j][0]) + abs(i[1] - k[j][1])
            min_dis = min(min_dis, dis)

        tmp += min_dis
    result = min(result, tmp)

print(result)