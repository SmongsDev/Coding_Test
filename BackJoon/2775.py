import sys

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    apate = [ x for x in range(1, n+1) ]
    for _ in range(k):
        for j in range(1, n):
            apate[j] += apate[j-1]
    print(apate[-1])
