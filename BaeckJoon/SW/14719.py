import sys; input = sys.stdin.readline
h, w = map(int,input().split())
wall = list(map(int,input().split()))
res = 0
for i in range(1, w-1):
    left = max(wall[:i])
    right = max(wall[i+1:])
    compare = min(left, right)
    if wall[i] < compare:
        res += compare - wall[i] 
print(res)