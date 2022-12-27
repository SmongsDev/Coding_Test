import sys

N = int(sys.stdin.readline())

N_list = [0]*10001

for _ in range(N):
    n = int(sys.stdin.readline())
    N_list[n] += 1
    
for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(i)
