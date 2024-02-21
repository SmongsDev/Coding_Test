import sys; input = sys.stdin.readline
n, m, p = map(int, input().split())

hateDic = {}
visited = [False] * n
board = []
for i in range(n):
    love, hate = map(int,input().split())
    hateIn = hateDic.get(hate, -1)
    if hateIn == -1:
        hateDic[hate] = i
    board.append((love,hate))

res = 0
while 1:
    hateIdx = hateDic.get(p, -1)

    if hateIdx == -1:
        print(res)
        break
    if visited[hateIdx]:
        print(-1)
        break
    else:
        visited[hateIdx] = True
        p = board[hateIdx][0]
    
    res += 1


# {2:0, 3:1}