import sys; input = sys.stdin.readline
n, m, p = map(int, input().split())

hateDic = {}
visitDic = {}
visited = [0 for i in range(n)]
board = []
for i in range(n):
    loveC, hateC = map(int, input().split())
    isIn = hateDic.get(hateC, -1)
    if isIn == -1:
        hateDic[hateC] = i
    board.append([loveC, hateC])

move = 0
while True:
    hatePerson = hateDic.get(p, -1)

    if hatePerson == -1:
        print(move)
        break
    
    if visited[hatePerson]:
        print('-1')
        break
    else:
        visited[hatePerson] = 1
    p = board[hatePerson][0]

    move+=1