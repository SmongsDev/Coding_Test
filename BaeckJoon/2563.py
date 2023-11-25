import sys

input = sys.stdin.readline

paper = [ [0] * 100 for _ in range(100) ]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(x,x+10):
        for k in range(y,y+10):
            paper[j][k] = 1

cnt = 0
for i in range(100):
    cnt += paper[i].count(1)
print(cnt)