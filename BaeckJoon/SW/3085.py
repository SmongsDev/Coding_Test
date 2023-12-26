import sys; input = sys.stdin.readline
n = int(input())
candy = [ list(input()) for _ in range(n) ]
directions = [(0,1),(1,0)]
maxCnt = 0

def candyCount():
    global maxCnt
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1

for x in range(n):
    for y in range(n):
        for d in range(2):
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            if 0 <= nx < n and 0 <= ny < n:
                candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]
                candyCount()
                candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]
print(maxCnt)