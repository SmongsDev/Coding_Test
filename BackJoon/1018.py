import sys

input = sys.stdin.readline

N, M = map(int, input().split())

chess = []
dp = []

for _ in range(N):
    chess.append(input())


for i in range(N-7):
    for j in range(M-7):
        index1 = 0
        index2 = 0
        for a in range(i, 8+i):
            for b in range(j, 8+j):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'W':
                        index1 += 1
                    elif chess[a][b] != 'B':
                        index2 += 1
                else:
                    if chess[a][b] != 'B':
                        index1 += 1
                    elif chess[a][b] != 'W':
                        index2 += 1
        dp.append(min(index1, index2))
        
print(min(dp))
