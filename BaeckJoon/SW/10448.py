import sys; input = sys.stdin.readline
T = int(input())
dp = [i*(i+1)//2 for i in range(1,46)]
res = [0] * 1001
for i in dp:
    for j in dp:
        for k in dp:
            num = i + j + k
            if num <= 1000:
                res[num] = 1
for _ in range(T):
    print(res[int(input())])