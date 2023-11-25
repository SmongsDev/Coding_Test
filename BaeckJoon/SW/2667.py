import sys

input = sys.stdin.readline

n = int(input())
graph = [ list(map(int, input().rstrip())) for _ in range(n) ]
cnt = []
count = 0

def dfs(x, y):
    if 0 > x or x >= n or 0 > y or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
    
total_cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            cnt.append(count)
            total_cnt += 1
            count = 0

print(total_cnt)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])